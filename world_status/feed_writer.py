from elasticsearch.helpers import bulk, BulkIndexError
from hashlib import md5
from world_status.es import get_elasticsearch, declare_schema
from world_status.indices.article import Article
from world_status.log import log


class FeedWriter:
    def __init__(self):
        self.es = get_elasticsearch()

        declare_schema(self.es, Article)

    def save(self, feed_contents):
        successes = set(i['url'] for i in feed_contents)

        try:
            bulk(self.es, self.get_insert_actions(feed_contents))
        except BulkIndexError as e:
            if not e.args[0].endswith("document(s) failed to index."):
                raise

            failed_urls = set(i['create']['data']['url'] for i in e.args[1])
            successes = successes.difference(failed_urls)

        log.info("Saved {} articles".format(len(successes)))

        results = []

        for i in feed_contents:
            if i['url'] in successes:
                results.append(i)

        return results

    def get_insert_actions(self, feed_contents):
        for article in feed_contents:
            pkey = md5(article['url'].encode("utf-8")).hexdigest()
            yield {
                "_source": article,
                '_op_type': 'create',
                "_id": pkey,
                "_index": Article.name,
                "_type": Article.doc_type
            }
