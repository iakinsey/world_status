from json import loads
from nltk import download, pos_tag, word_tokenize, ngrams
from pathlib import Path
from os.path import exists, join
from re import compile, split, sub
from world_status import config


if not exists(join(Path.home(), 'nltk_data')):
    download('all')


USEFUL_TAGS = set(["NNP"])
IGNORE_WORDS = set(loads(open(config.IGNORE_WORDS_PATH).read()))
STOP_PUNCTUATION = ":;,.!?"
PUNCTUATION_PATTERN = compile(''.join([
    "[\\",
    "\\".join([i for i in STOP_PUNCTUATION]),
    "]"
]))
GOOD_CHARS = r'[^ a-zA-Z0-9]'

def get_useful_terms(text):
    tags = pos_tag(word_tokenize(text))
    useful_words = set()

    for word, tag in tags:
        if tag in USEFUL_TAGS and word.lower() not in IGNORE_WORDS:
            useful_words.add(word)

    return " ".join(useful_words)


def get_ngrams(text, n=3):
    sections = split(PUNCTUATION_PATTERN, text.lower())

    for section in sections:
        if not section:
            continue

        section = sub(GOOD_CHARS, "", section)
        tokens = word_tokenize(section)

        for ngram in ngrams(tokens, n):
            result = config.TERM_DELIMITER.join(ngram)

            if config.TERM_DELIMITER in result:
                yield result
