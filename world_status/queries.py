def get_uesful_terms(size=25):
    return {
        "aggs": {
            "tagcloud": {
                "terms": {
                    "field": "useful_terms",
                    "size": size
                }
            }
        }
    }
