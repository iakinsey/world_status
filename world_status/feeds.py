from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta, datetime
from feedparser import parse
from random import randrange
from world_status import config
from world_status.log import log


class FeedManager:
    _feeds = None

    def __init__(self, feed_urls):
        self.feed_urls = feed_urls

    def get_feed_content(self, feed_url):
        log.info("Get feed metadata from {}".format(feed_url))

        rss_feed = parse(feed_url)
        ttl = self._get_ttl(rss_feed)
        name = rss_feed.get("feed", {}).get("title") or feed_url

        return {
            "name": name,
            "url": feed_url,
            "ttl": ttl,
            "last_updated": datetime.min
        }

    def _init_feeds(self):
        self._feeds = {}

        thread_count = config.STATUS_JOB_THREAD_COUNT

        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            for content in executor.map(self.get_feed_content, self.feed_urls):
                url = content['url']
                self._feeds[url] = content

                yield (url, content)

    @property
    def feeds(self):
        if self._feeds is None:
            return self._init_feeds()

        return self._feeds.items()

    @property
    def feeds_with_expired_ttls(self):
        now = datetime.now()

        for url, meta in self.feeds:
            if meta['last_updated'] + meta['ttl'] <= now:
                yield url

    def _get_ttl(self, rss_feed):
        default_ttl = randrange(
            0 if config.DEFAULT_TTL - 2 < 0 else config.DEFAULT_TTL - 2,
            config.DEFAULT_TTL + 2
        )

        ttl = rss_feed.get("feed", {}).get("ttl", default_ttl)

        try:
            ttl = int(ttl)
        except:
            ttl = config.default_ttl

        return timedelta(minutes=ttl)

    def update_last_run_time(self, url):
        dict(self.feeds)[url]['last_updated'] = datetime.now()
