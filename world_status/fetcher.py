from bs4 import BeautifulSoup
from feedparser import parse
from textblob import TextBlob
from time import time
from warnings import catch_warnings, simplefilter
from world_status import config
from world_status.country import CountryMetaExtractor
from world_status.log import log
from world_status.terms import get_ngrams


def get_content(url):
    log.info("Fetching feed from {}".format(url))
    contents = parse(url)
    entries = contents.get("entries", [])
    result = []

    for entry in entries:
        extractor = EntityContentExtractor(url)
        entity = extractor.get_entity(entry)

        if len(entity) > 0:
            result.append(entity)

    return result


class EntityContentExtractor:
    country_meta = CountryMetaExtractor(config.COUNTRY_NAME_PATH)

    def __init__(self, url):
        self.url = url
        self.countries = set()
        self.all_text_list = []
        self.entity = {"created": int(time())}

    def get_entity(self, entry):
        summary = entry.get("summary")
        content = entry.get("content")
        title = entry.get("title")
        tags = entry.get("tags")
        url = entry.get("link")

        if url:
            self.entity['url'] = url

        if summary:
            self.analyze('summary', summary)

        if title:
            self.analyze('title', title)

        if content:
            self.analyze_content(content)

        if tags:
            self.analyze_tags(tags)

        if self.all_text_list:
            all_text = "; ".join(self.all_text_list)
            self.entity['all_text'] = all_text
            self.entity['ngrams'] = list(get_ngrams(all_text))
            self.analyze_countries()

        return self.entity

    def analyze_countries(self):
        string = self.entity['all_text']
        countries = self.country_meta.get_countries(string)

        if countries:
            self.entity['countries'] = list(countries)

    def analyze_content(self, content):
        tokens = []

        for i in content:
            if not i:
                continue

            value = i.get("value")
            tokens.append(value)

        if tokens:
            self.analyze('content', " ".join(tokens))

    def analyze_tags(self, rss_tags):
        result = []

        for tag in rss_tags:
            value = tag.get("term")

            if not value:
                continue

            result.append(value)

        if result:
            self.entity['tags'] = result
            self.all_text_list.append("; ".join(result))

    def get_raw_text(self, text):
        with catch_warnings():
            simplefilter("ignore")
            raw_text = BeautifulSoup(text).get_text()

        return raw_text.replace("\n", " ").replace("\t", " ")

    def get_sentiment(self, text):
        analysis = TextBlob(text)
        sentiment = analysis.sentiment

        return sentiment.polarity, sentiment.subjectivity

    def analyze(self, prefix, text):
        raw_text = self.get_raw_text(text)
        polarity, sentiment = self.get_sentiment(raw_text)
        countries = self.country_meta.get_countries(text)

        result = {
            "text": raw_text,
            "polarity": polarity,
            "sentiment": sentiment
        }

        self.all_text_list.append(raw_text)

        for key, value in result.items():
            self.entity[prefix + "_" + key] = value
