from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
from world_status.config import ES_CLUSTER
from logging import getLogger, ERROR
from warnings import catch_warnings, simplefilter


def get_elasticsearch():
    loggers = ('elasticsearch', 'urllib3.connectionpool')

    for name in loggers:
        logger = getLogger(name)
        logger.setLevel(ERROR)

    with catch_warnings():
        simplefilter('ignore')
        es = Elasticsearch(ES_CLUSTER)

    return es


def get_hits(result):
    for datum in result['hits']['hits']:
        yield datum['_source']


def declare_schema(es, Index):
    try:
        es.indices.create(index=Index.name, body=Index.definition)
    except RequestError as e:
        if e.error != 'resource_already_exists_exception':
            raise


def query_and_get_hits(Index, query):
    es = get_elasticsearch()
    result = es.search(index=Index.name, body=query)

    return get_hits(result)
