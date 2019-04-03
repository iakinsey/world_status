from world_status import config
from world_status.indices.article import Article
from world_status.fetcher import get_content
from world_status.feeds import FeedManager
from world_status.feed_writer import FeedWriter


class FeedIngestionJob:
    def __init__(self):
        self.feed_manager = FeedManager(config.RSS_FEEDS)
        self.feed_writer = FeedWriter()

    def run(self):
        while 1:
            try:
                self.do_work()
            except (KeyboardInterrupt, SystemExit):
                exit(0)
            except Exception as e:
                print(e)

    def do_work(self):
       for url in self.feed_manager.feeds_with_expired_ttls:
            content = get_content(url)
            self.feed_writer.save(content)
            self.feed_manager.update_last_run_time(url)
