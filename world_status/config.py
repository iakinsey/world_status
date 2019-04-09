from os.path import abspath, dirname, join, realpath


###############################################################################
# Paths
###############################################################################


PROJECT_ROOT = abspath(dirname(dirname(realpath(__file__))))
DATA_DIR = join(PROJECT_ROOT, 'config')
COUNTRY_NAME_PATH = join(DATA_DIR, 'countries.json')
DEBUG = False

###############################################################################
# Feeds
###############################################################################


RSS_FEEDS = [
    "http://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
    "https://www.latimes.com/rss2.0.xml",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "http://feeds.bbci.co.uk/news/rss.xml",
    "http://feeds.reuters.com/Reuters/worldNews",
    "http://feeds.washingtonpost.com/rss/world",
    "http://feeds.washingtonpost.com/rss/rss_blogpost",
    "https://www.yahoo.com/news/rss/world",
    "http://rss.cnn.com/rss/edition_world.rss",
    "http://rssfeeds.usatoday.com/usatoday-newstopstories&x=1",
    "https://www.yahoo.com/news/rss/",
    "http://feeds.reuters.com/Reuters/domesticNews",
    "http://feeds.skynews.com/feeds/rss/us.xml",
    "http://rss.cnn.com/rss/edition_us.rss",
    "http://feeds.skynews.com/feeds/rss/uk.xml",
    "http://feeds.reuters.com/reuters/UKdomesticNews",
    "https://www.theguardian.com/uk/rss",
    "https://techcrunch.com/rssfeeds/",
    "http://rss.slashdot.org/Slashdot/slashdot",
    "https://spectrum.ieee.org/rss/blog/tech-talk/fulltext",
    "https://www.techworld.com/news/rss",
    "https://www.wired.com/feed",
    "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
]


ES_CLUSTER = ['localhost:9200']


DEFAULT_TTL = 60
JOB_RUN_INTERVAL_SECONDS = 240


###############################################################################
# Notifier
###############################################################################


NOTIFIER_ZMQ_HOST = "0.0.0.0"
NOTIFIER_ZMQ_PORT = 32112
NOTIFIER_WEBSOCKET_HOST = "0.0.0.0"
NOTIFIER_WEBSOCKET_PORT = 5321
