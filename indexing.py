from elasticsearch import Elasticsearch as es

es_client = es(
    ["https://host.com:9243"],
    http_auth=('user', 'password')
)

field_name = "field_name"
field_value = 4
document = {
    "another_field_name": "another_field_value",
    field_name: field_value
}

#In most cases, it's better to let Elasticsearch create its own ID.
response = es_client.index(index="index_name", id="id_example", document=document)
print(response)

response = es_client.get(index="index_name", id="id_example")
print(response)
