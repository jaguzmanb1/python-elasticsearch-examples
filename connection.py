
from elasticsearch import Elasticsearch as es

es_client = es(
    ["https://host.com:9243"],
    http_auth=('user', 'password')
)

print(es_client.info())

# Basic auth
es_client = es(
    ["https://user:password@host.com:9243"]
)

print(es_client.info())

# Unsecure connection
es_client = es(
    ["http://user:password@host.com:9243"],
    verify_certs=False
)

print(es_client.info())
