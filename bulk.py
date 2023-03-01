from elasticsearch import Elasticsearch as es
from elasticsearch.helpers import bulk

es_client = es(
    ["https://host.com:443"],
    http_auth=('user', 'password')
)


def create_documents():
    for i in range(100000):
        yield {
            "_index": "index_name",
            "_id": i,
            "_op_type": "index",
            "_source": {
                "field_name": i
            }
        }


response = bulk(es_client, create_documents())
print(response)

def update_documents():
    for i in range(10):
        yield {
            "_index": "index_name",
            "_id": i,
            "_op_type": "update",
            "doc": {
                "new_field": i * i
            }
        }


response = bulk(es_client, create_documents())
print(response)

response = bulk(es_client, update_documents())
print(response)