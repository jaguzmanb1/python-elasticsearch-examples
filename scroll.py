from elasticsearch import Elasticsearch as es

es_client = es(
    ["https://host.com:9243"],
    http_auth=('user', 'password')
)

def process_data(datos):
    for doc in datos:
        print(doc)


scroll_size = 10000
scroll_time = "2m"

# First scroll page
data = es_client.search(
    index="indice_ejemplo",
    scroll=scroll_time,
    size=scroll_size
)

# Next scroll search id
scroll_id = data['_scroll_id']
request_size = len(data['hits']['hits'])

# Is there any more data? 
while request_size > 0:
    process_data(data['hits']['hits'])

    data = es_client.scroll(scroll_id=scroll_id, scroll=scroll_time)

    scroll_id = data['_scroll_id']

    request_size = len(data['hits']['hits'])