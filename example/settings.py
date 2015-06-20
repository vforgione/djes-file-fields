import os


DATABASES = {
    "default": {
        "NAME": "default",
        "ENGINE": "django.db.backends.sqlite3"
    }
}

INSTALLED_APPS = (
    "djes_file_fields",
    "example.app",
)

SECRET_KEY = "Oh man, they'll never break this one!"

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware"
)

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")

ES_INDEX = "djes-file-fields-example"

ES_INDEX_SETTINGS = {
    "djes-file-fields-example": {
        "index": {
            "number_of_replicas": 1,
            "analysis": {
                "filter": {
                    "autocomplete_filter": {
                        "type": "edge_ngram",
                        "min_gram": 1,
                        "max_gram": 20
                    }
                },
                "analyzer": {
                    "autocomplete": {
                        "type":      "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "lowercase",
                            "autocomplete_filter"
                        ]
                    }
                }
            }
        },
    }
}
