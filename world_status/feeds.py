from datetime import timedelta, datetime
from feedparser import parse
from random import randrange
from world_status import config


class FeedManager:
    _feeds = None

    def __init__(self, feed_urls):
        self.feed_urls = feed_urls

    def get_feed_content(self, feed_url):
        rss_feed = parse(feed_url)
        ttl = self._get_ttl(rss_feed)
        name = rss_feed.get("feed", {}).get("title") or feed_url

        return {
            "name": name,
            "url": feed_url,
            "ttl": ttl,
            "last_updated": datetime.min
        }

    @property
    def feeds(self):
        if self._feeds is None:
            self._feeds = {u: self.get_feed_content(u) for u in self.feed_urls}

        return self._feeds

    @property
    def feeds_with_expired_ttls(self):
        now = datetime.now()

        return {
            url: meta
            for url, meta in self.feeds.items()
            if meta['last_updated'] + meta['ttl'] <= now
        }

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

        return timedelta(ttl)

    def update_last_run_time(self, url):
        self.feeds[url]['last_updated'] = datetime.now()
