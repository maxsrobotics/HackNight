import digikey
from digikey.v3.productinformation import KeywordSearchRequest
import os
import ast
import sys

search = " ".join(sys.argv[1:])  # Join all elements from index 1 to the end

os.environ["DIGIKEY_CLIENT_ID"] = "QlnQBYLGQCUJPG2xAydT5zUbrSzsARya"
os.environ["DIGIKEY_CLIENT_SECRET"] = "pCN17uORphL5KIys"
os.environ['DIGIKEY_STORAGE_PATH'] = "cache_dir"

search_requests = KeywordSearchRequest(keywords=search, record_count=10)
results = digikey.keyword_search(body=search_requests)

parsed = ast.literal_eval(str(results))

outputDict = {}

for i in range(len(parsed['products'])):
   
    # Create a new dictionary for each product
    product_dict = {
        'unit_price': str(parsed['products'][i]['unit_price']),
        'quantity': str(parsed['products'][i]['minimum_order_quantity']),
        'partNum': str(parsed['products'][i]['manufacturer_part_number'])
    }
    
    # Append the duct dictionary to the output dictionary
    outputDict[i] = product_dict

# print(outputDict)

specified_quantity = 10  # Replace with your specified quantity

# Filter the dictionary to only include items with a quantity greater than or equal to the specified quantity
outputDict = {k: v for k, v in outputDict.items() if int(v['quantity']) <= specified_quantity}

print(outputDict)