from asyncio import get_event_loop, new_event_loop, Queue
from base64 import b64decode
from collections import defaultdict
from elasticsearch_async import AsyncElasticsearch
from json import dumps, loads
from uuid import uuid4
from websockets import serve
from world_status import config
from world_status.indices.article import Article
from world_status.log import log
from world_status.queries import get_articles, get_prominent_terms
from zmq import PULL
from zmq.asyncio import Context


QUEUES = defaultdict(list)


def get_filter(path):
    cleaned_path = path.strip("/")

    if not cleaned_path:
        return {}

    return loads(b64decode(cleaned_path))


def message_is_relevant(message, filter):
    """
    Filters follow the following pattern:

    tag IN tags AND country IN countries AND term IN terms
    """

    if not filter:
        return True

    tag_filter = filter.get("tags", [])
    country_filter = filter.get("countries", [])
    term_filter = filter.get("terms", [])
    matches_tag = not tag_filter
    matches_country = not country_filter
    matches_term = not term_filter
    tags = message.get("tags", [])
    countries = message.get("countries", [])
    text_content = message.get("all_text", "")

    for tag in tag_filter:
        if tag in tags:
            matches_tag = True
            break

    for country in country_filter:
        if country in countries:
            matches_country = True
            break

    for term in term_filter:
        if term in text_content:
            matches_term = True
            break

    return matches_term and matches_country and matches_tag


def register_queue(uuid, queue, path):
    QUEUES[uuid] = {
        "queue": queue,
        "filter": get_filter(path)
    }


def unregister_queue(uuid):
    del QUEUES[uuid]


async def publish_message(message):
    for meta in QUEUES.values():
        queue = meta['queue']
        filter = meta['filter']

        if message['message_type'] == "article":
            if message_is_relevant(message['data'], filter):
                if 'all_text' in message['data']:
                    del message['data']['all_text']

                await queue.put(message)


async def send_initial_messages(uuid, websocket):
    filter = QUEUES[uuid]['filter']
    es_query = get_articles(filter)
    es = AsyncElasticsearch(hosts=config.ES_CLUSTER)
    results = await es.search(index=Article.name, body=es_query)
    data = results['hits']['hits']

    for message in data:
        await websocket.send(dumps({
            "message_type": "article",
            "data": message['_source']
        }))

    await send_tag_cloud(uuid, websocket)


async def send_tag_cloud(uuid, websocket):
    filter = QUEUES[uuid]['filter']
    es_query = get_prominent_terms(filter)
    import pprint
    pprint.pprint(es_query)
    es = AsyncElasticsearch(hosts=config.ES_CLUSTER)
    results = await es.search(index=Article.name, body=es_query)
    data = results['aggregations']['tagcloud']['buckets']
    results = []

    for entity in data:
        results.append({
            "count": entity['doc_count'],
            "term": entity['key'].replace(config.TERM_DELIMITER, ' ')
        })

    await websocket.send(dumps({
        "message_type": "tag_cloud",
        "data": results
    }))


async def producer_handler(websocket, path):
    queue = Queue(loop=get_event_loop())
    uuid = str(uuid4())
    count = 0

    register_queue(uuid, queue, path)
    await send_initial_messages(uuid, websocket)

    try:
        while 1:
            msg = await queue.get()

            await websocket.send(dumps(msg))

            count += 1

            if count == 100:
                count = 0
                await send_tag_cloud(uuid, websocket)

    finally:
        unregister_queue(uuid)


async def start_listening_server(host, port):
    uri = "tcp://{}:{}".format(host, port)
    context = Context()
    receiver = context.socket(PULL)
    receiver.bind(uri)

    log.info("Listening server started on {}:{}".format(host, port))

    while 1:
        message = await receiver.recv_json()
        await publish_message(message)


def start_websocket_server(host, port, loop):
    start_server = serve(producer_handler, host, port, loop=loop)
    loop.run_until_complete(start_server)
    log.info("Websocket server started on {}:{}".format(host, port))


def start():
   loop = new_event_loop()
   listening_server_coro = start_listening_server(
       config.NOTIFIER_ZMQ_HOST,
       config.NOTIFIER_ZMQ_PORT
   )

   start_websocket_server(
       config.NOTIFIER_WEBSOCKET_HOST,
       config.NOTIFIER_WEBSOCKET_PORT,
       loop
   )
   loop.run_until_complete(listening_server_coro)
