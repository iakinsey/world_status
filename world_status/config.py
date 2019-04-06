from os.path import abspath, dirname, join, realpath


###############################################################################
# Paths
###############################################################################


PROJECT_ROOT = abspath(dirname(dirname(realpath(__file__))))
DATA_DIR = join(PROJECT_ROOT, 'config')
COUNTRY_NAME_PATH = join(DATA_DIR, 'countries.json')


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
