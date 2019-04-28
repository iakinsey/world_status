def get_prominent_terms(filter=None, size=25):
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

    if filter:
        query.update(get_articles(filter))

    return query


def get_articles(filter):
    should = []
    tag_filter = filter.get("tags", [])
    country_filter = filter.get("countries", [])
    term_filter = filter.get("terms", [])

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

    return {
        'query': {
            'constant_score': {
                'filter': {
                    'bool': {
                        'should': should
                    }
                }
            }
        },
        'from': 0,
        'size': 10000,
        "sort": [
            {"created": "desc"}
        ],
        "_source": {
            "exclude": ["all_text"]
        }
    }
