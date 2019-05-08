from time import time


def get_prominent_terms(filter=None, size=25):
    if filter is None:
        filter = {}

    query = {
        "aggs": {
            "tagcloud": {
                "terms": {
                    "field": "ngrams",
                    "size": size
                }
            }
        }
    }

    query.update(get_articles(filter))

    return query


def get_articles(filter, size=10000):
    should = []
    must = {}
    tag_filter = filter.get("tags", [])
    country_filter = filter.get("countries", [])
    term_filter = filter.get("terms", [])
    time_filter = filter.get("time", int(time() - 604800))

    term_queries = []
    country_queries = []
    tag_queries = []

    for term in term_filter:
        term_queries.append({"match": {"all_text": {"query": term}}})

    for country in country_filter:
        country_queries.append({
            "match_phrase": {"countries": country}
        })

    for tag in tag_filter:
        tag_queries.append({
            "match_phrase": {"tags": tag}
        })

    for query in [term_queries, country_queries, tag_queries]:
        if not query:
            continue

        should.append({
            "bool": {"must": query}
        })

    if time_filter:
        must["range"] = {"created": {"gte": time_filter}}

    return {
        'query': {
            'constant_score': {
                'filter': {
                    'bool': {
                        'should': should,
                        'must': must
                    }
                }
            }
        },
        'from': 0,
        'size': size,
        "sort": [
            {"created": "desc"}
        ],
        "_source": {
            "exclude": ["all_text"]
        }
    }
