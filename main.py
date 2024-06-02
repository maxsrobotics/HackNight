import digikey

from digikey.v3.productinformation import KeywordSearchRequest
from digikey.v3.productinformation.rest import ApiException
from digikey.oauth import get_digikey_client

# Create a client
client = get_digikey_client()

# Create a keyword search request
search_request = KeywordSearchRequest(keywords='resistor', records=10)

try:
    # Perform the search
    api_response = client.keyword_search(body=search_request)
    print("Search completed successfully")
    for product in api_response.products:
        print(f"Found product: {product.digi_key_part_number}")
except ApiException as e:
    print("Exception when calling Digikey API: %s\n" % e)