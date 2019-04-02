from json import loads
from re import compile


class CountryMetaExtractor:
    _regex_template = "\\b(?:{})\\b"

    def __init__(self, config_path):
        self.config = loads(open(config_path).read())
        self._compile_regexes()

    def _compile_regexes(self):
        for iso3166_alpha_2, config in self.config.items():
            names = config.get("names")

            if not names:
                continue

            regex = compile(self._regex_template.format("|".join(names)))
            config['names_regex'] = regex

    def get_countries(self, string):
        matches = set()

        for iso3166_alpha_2, config in self.config.items():
            regex = config.get("names_regex")

            if regex is None:
                continue

            match = regex.search(string)

            if match:
                matches.add(iso3166_alpha_2)

        return matches
