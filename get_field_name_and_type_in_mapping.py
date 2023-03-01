mapping = {
    "properties" : {
        "@timestamp" : {
          "type" : "date"
        },
        "@version" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "description" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "id" : {
          "type" : "long"
        }
    }
}

def accessObjectField(pRoot, pJson):
    for field in pJson:
        if field is "properties" or "type" not in pJson[field]:
            fieldName = "" + pRoot if (field is "properties") else pRoot + field
            accessObjectField(fieldName , pJson[field])
        else:
            fieldName = pRoot + field if (pRoot is "") else pRoot + "." + field
            print(fieldName + " - " + pJson[field]["type"])
            if ("fields" in pJson[field]):
                fieldName = "" + field if (pRoot is "") else pRoot + "." + field
                accessObjectField(fieldName, pJson[field]["fields"])


accessObjectField("", mapping)
