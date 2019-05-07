from multiprocessing import cpu_count
from os.path import abspath, dirname, join, realpath


###############################################################################
# Paths
###############################################################################


PROJECT_ROOT = abspath(dirname(dirname(realpath(__file__))))
DATA_DIR = join(PROJECT_ROOT, 'config')
COUNTRY_NAME_PATH = join(DATA_DIR, 'countries.json')
IGNORE_WORDS_PATH = join(DATA_DIR, 'ignore_words.json')
USELESS_TERMS_PATH = join(DATA_DIR, 'ngram_useless_terms.json')
BAD_NGRAMS_PATH = join(DATA_DIR, 'bad_ngrams.json')


###############################################################################
# System stuff
###############################################################################


DEBUG = False
STATUS_JOB_THREAD_COUNT = cpu_count()


###############################################################################
# Feeds
###############################################################################


RSS_FEEDS = [
    'http://blog.ap.org/feed.rss',
    'http://blog.archive.org/feed/',
    'http://en.rian.ru/export/rss2/index.xml',
    'http://feeds.abcnews.com/abcnews/politicsheadlines',
    'http://feeds.bbci.co.uk/news/business/rss.xml',
    'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml',
    'http://feeds.bbci.co.uk/news/rss.xml',
    'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
    'http://feeds.bbci.co.uk/news/technology/rss.xml',
    'http://feeds.bbci.co.uk/news/world/rss.xml',
    'http://feeds.feedburner.com/JamesFallows',
    'http://feeds.feedburner.com/JonathanChaitRssFeed',
    'http://feeds.feedburner.com/PoliticalWire',
    'http://feeds.feedburner.com/TheWirecutter',
    'http://feeds.feedburner.com/Torrentfreak',
    'http://feeds.feedburner.com/avc',
    'http://feeds.feedburner.com/fastcompany/headlines',
    'http://feeds.feedburner.com/pbs/mediashift-blog',
    'http://feeds.feedburner.com/realclearpolitics/qlMj',
    'http://feeds.feedburner.com/scotusblog/pFXs',
    'http://feeds.feedburner.com/talking-points-memo',
    'http://feeds.feedburner.com/thedailybeast/articles',
    'http://feeds.foxnews.com/foxnews/latest',
    'http://feeds.foxnews.com/foxnews/politics?format=xml',
    'http://feeds.latimes.com/movies/reviews/',
    'http://feeds.nytimes.com/nyt/rss/Books',
    'http://feeds.publicradio.org/public_feeds/apm-reports/rss/rss',
    'http://feeds.reuters.com/Reuters/domesticNews',
    'http://feeds.reuters.com/Reuters/worldNews',
    'http://feeds.reuters.com/reuters/INbusinessNews',
    'http://feeds.reuters.com/reuters/UKdomesticNews',
    'http://feeds.reuters.com/reuters/worldNews',
    'http://feeds.skynews.com/feeds/rss/uk.xml',
    'http://feeds.skynews.com/feeds/rss/us.xml',
    'http://feeds.washingtonpost.com/rss/entertainment',
    'http://feeds.washingtonpost.com/rss/lifestyle',
    'http://feeds.washingtonpost.com/rss/local',
    'http://feeds.washingtonpost.com/rss/national',
    'http://feeds.washingtonpost.com/rss/opinions',
    'http://feeds.washingtonpost.com/rss/politics',
    'http://feeds.washingtonpost.com/rss/rss_blogpost',
    'http://feeds.washingtonpost.com/rss/rss_capital-weather-gang',
    'http://feeds.washingtonpost.com/rss/rss_early-lead',
    'http://feeds.washingtonpost.com/rss/rss_right-turn',
    'http://feeds.washingtonpost.com/rss/rss_the-fix',
    'http://feeds.washingtonpost.com/rss/sports/blogs-columns',
    'http://feeds.washingtonpost.com/rss/world',
    'http://georgelakoff.com/feed/',
    'http://hnrss.org/newest?points=200',
    'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
    'http://hosted2.ap.org/atom/APDEFAULT/495d344a0d10421e9baa8ee77029cfbd',
    'http://hosted2.ap.org/atom/APDEFAULT/89ae8247abe8493fae24405546e9a1aa',
    'http://hosted2.ap.org/atom/APDEFAULT/f70471f764144b2fab526d39972d37b3',
    'http://krugman.blogs.nytimes.com/feed/',
    'http://mediagazer.com/feed.xml',
    'http://mondaynote.com/feed',
    'http://motherboard.vice.com/en_us/rss',
    'http://om.co/feed/',
    'http://pressthink.org/feed/',
    'http://qz.com/feed/',
    'http://radio3.io/users/davewiner/rss.xml',
    'http://rss.cbc.ca/lineup/world.xml',
    'http://rss.cnn.com/rss/edition_us.rss',
    'http://rss.cnn.com/rss/edition_world.rss',
    'http://rss.dw.de/rdf/rss-en-world',
    'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
    'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
    'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'http://rss.nytimes.com/services/xml/rss/nyt/sunday-review.xml',
    'http://rss.slashdot.org/Slashdot/slashdot',
    'http://rssfeeds.usatoday.com/UsatodaycomMovies-TopStories',
    'http://rssfeeds.usatoday.com/usatoday-newstopstories&x=1',
    'http://stratechery.com/feed/',
    'http://talkingpointsmemo.com/feed/all',
    'http://thinkprogress.org/feed',
    'http://truth-out.org/feed?format=feed',
    'http://www.aclu.org/taxonomy/feed-term/362/feed',
    'http://www.aljazeera.com/Services/Rss/?PostingId=2007731105943979989',
    'http://www.axios.com/feeds/feed.rss',
    'http://www.ben-evans.com/benedictevans?format=RSS',
    'http://www.businessoffashion.com/syndication/feed',
    'http://www.buzzfeed.com/tech.xml',
    'http://www.cbc.ca/cmlink/rss-canada',
    'http://www.cbc.ca/cmlink/rss-technology',
    'http://www.cbc.ca/cmlink/rss-topstories',
    'http://www.cbc.ca/cmlink/rss-world',
    'http://www.cbsnews.com/latest/rss/face-the-nation',
    'http://www.cbsnews.com/latest/rss/politics',
    'http://www.dailywire.com/rss.xml',
    'http://www.economist.com/sections/business-finance/rss.xml',
    'http://www.engadget.com/rss.xml',
    'http://www.europeanvoice.com/feed/',
    'http://www.internethistorypodcast.com/feed/',
    'http://www.memeorandum.com/feed.xml',
    'http://www.niemanlab.org/feed/',
    'http://www.npr.org/rss/rss.php?id=1014',
    'http://www.nytimes.com/services/xml/rss/nyt/Americas.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Arts.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/DiningandWine.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Europe.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Health.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Movies.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Obituaries.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Opinion.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Science.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Sports.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Television.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/TheCity.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/Theater.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/World.xml',
    'http://www.nytimes.com/services/xml/rss/nyt/WorldBusiness.xml',
    'http://www.nytimes.com/svc/collections/v1/publish/'
    'http://www.nytimes.com/by/dan-barry/rss.xml',
    'http://www.politico.com/rss/politicopicks.xml',
    'http://www.poynter.org/feed/',
    'http://www.slate.com/articles/news_and_politics.fulltext.all.rss',
    'http://www.spiegel.de/international/business/index.rss',
    'http://www.spiegel.de/international/europe/index.rss',
    'http://www.spiegel.de/international/index.rss',
    'http://www.techmeme.com/index.xml',
    'http://www.theatlantic.com/feed/all/',
    'http://www.theguardian.com/books/rss',
    'http://www.theguardian.com/business/economics/rss',
    'http://www.theguardian.com/lifeandstyle/women/rss',
    'http://www.theguardian.com/music/rss',
    'http://www.theguardian.com/stage/rss',
    'http://www.theguardian.com/tv-and-radio/rss',
    'http://www.theguardian.com/uk-news/rss',
    'http://www.theguardian.com/us/film/rss',
    'http://www.theguardian.com/world/americas/rss',
    'http://www.theguardian.com/world/asia/rss',
    'http://www.theguardian.com/world/europe-news/rss',
    'http://www.theguardian.com/world/middleeast/rss',
    'http://www.variety.com/rss.asp?categoryid=10',
    'http://www.vox.com/rss/index.xml',
    'http://www.wired.com/feed/',
    'http://www.wsj.com/xml/rss/3_7041.xml',
    'https://blog.ap.org/feed.rss',
    'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
    'https://feeds.a.dj.com/rss/RSSWorldNews.xml',
    'https://news.ycombinator.com/rss',
    'https://spectrum.ieee.org/rss/blog/tech-talk/fulltext',
    'https://techcrunch.com/rssfeeds/',
    'https://www.aljazeera.com/xml/rss/all.xml',
    'https://www.cnbc.com/id/100003114/device/rss/rss.html',
    'https://www.cnbc.com/id/100727362/device/rss/rss.html',
    'https://www.dailymail.co.uk/articles.rss',
    'https://www.dailymail.co.uk/news/index.rss',
    'https://www.huffpost.com/section/front-page/feed',
    'https://www.latimes.com/rss2.0.xml',
    'https://www.rt.com/rss/',
    'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml',
    'https://www.techworld.com/news/rss',
    'https://www.theguardian.com/uk/rss',
    'https://www.wired.com/feed',
    'https://www.yahoo.com/news/rss/',
    'https://www.yahoo.com/news/rss/world'
]

ES_CLUSTER = ['localhost:9200']
TERM_DELIMITER = "0000"


DEFAULT_TTL = 60
JOB_RUN_INTERVAL_SECONDS = 240


###############################################################################
# Notifier
###############################################################################


NOTIFIER_ZMQ_HOST = "0.0.0.0"
NOTIFIER_ZMQ_PORT = 32112
NOTIFIER_WEBSOCKET_HOST = "0.0.0.0"
NOTIFIER_WEBSOCKET_PORT = 5321
