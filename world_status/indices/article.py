class Article:
    name = "article"
    doc_type = "resource"
    definition = {
        "mappings": {
            doc_type: {
                "properties": {
                    "url": {"type": "keyword"},
                    "summary_text": {"type": "text"},
                    "summary_polarity": {"type": "float"},
                    "summary_sentiment": {"type": "float"},
                    "title_text": {"type": "text"},
                    "title_polarity": {"type": "float"},
                    "title_sentiment": {"type": "float"},
                    "content_text": {"type": "text"},
                    "content_polarity": {"type": "float"},
                    "content_sentiment": {"type": "float"}
                }
            }
        }
    }
