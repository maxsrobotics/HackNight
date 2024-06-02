import digikey
from digikey.v3.productinformation import KeywordSearchRequest
import os
import json

value = "10uF"
partType = "ceramic capacitor"

# Assuming you have a JSON object
json_object = {"value": value, "partType": partType}

# Pretty print the JSON
pretty_json = json.dumps(json_object, indent=4)
print(pretty_json["value"])