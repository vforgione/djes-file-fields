from djes.management.commands.sync_es import get_indexes, sync_index
from elasticsearch_dsl.connections import connections
import pytest


@pytest.fixture(scope="module")
def es_client(request):
    es = connections.get_connection("default")
    indexes = get_indexes()

    for index in list(indexes):
        es.indices.delete_alias("{}_*".format(index), "_all", ignore=[404])
        es.indices.delete("{}_*".format(index), ignore=[404])

    for index, body in indexes.items():
        sync_index(index, body)

    def fin():
        for index in list(indexes):
            es.indices.delete_alias("{}_*".format(index), "_all", ignore=[404])
            es.indices.delete("{}_*".format(index), ignore=[404])

    request.addfinalizer(fin)
    return es
