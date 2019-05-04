from concurrent.futures import ThreadPoolExecutor
from time import sleep
from world_status import config
from world_status.indices.article import Article
from world_status.fetcher import get_content
from world_status.feeds import FeedManager
from world_status.feed_writer import FeedWriter
from world_status.log import log
from world_status.publisher import Publisher


class FeedIngestionJob:
    def __init__(self):
        self.thread_count = config.STATUS_JOB_THREAD_COUNT
        self.feed_manager = FeedManager(config.RSS_FEEDS)
        self.feed_writer = FeedWriter()
        self.publisher = Publisher(
            config.NOTIFIER_ZMQ_HOST,
            config.NOTIFIER_ZMQ_PORT
        )

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

            sleep(config.JOB_RUN_INTERVAL_SECONDS)

    def do_work(self):
        feeds = self.feed_manager.feeds_with_expired_ttls

        with ThreadPoolExecutor(max_workers=self.thread_count) as executor:
            executor.map(self.get_content_notify_and_save, feeds)

    def get_content_notify_and_save(self, url):
        content = get_content(url)
        new_content = self.feed_writer.save(content)

        self.feed_manager.update_last_run_time(url)

        log.info("Publishing {} messages".format(len(new_content)))

        for content in new_content:
            self.publisher.publish(content, "article")
