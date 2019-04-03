from time import sleep
from world_status import config
from world_status.indices.article import Article
from world_status.fetcher import get_content
from world_status.feeds import FeedManager
from world_status.feed_writer import FeedWriter
from world_status.log import log


class FeedIngestionJob:
    def __init__(self):
        self.feed_manager = FeedManager(config.RSS_FEEDS)
        self.feed_writer = FeedWriter()

    def run(self):
        log.info("Starting feed ingestion job")

        while 1:
            log.info("Running job iteration")
            try:
                self.do_work()
            except (KeyboardInterrupt, SystemExit) as e:
                log.info("Caught SIGTERM, exiting")
                exit(0)
            except Exception as e:
                log.info("Caught error during processing")
                log.exception(e)

            sleep(10)

    def do_work(self):
        feeds = self.feed_manager.feeds_with_expired_ttls
        feed_count = len(feeds)

        if feed_count:
            log.info("Processing {} feeds".format(feed_count))

        for url in feeds:
            content = get_content(url)
            self.feed_writer.save(content)
            self.feed_manager.update_last_run_time(url)
