from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
# Defining the host, defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)


# Enter a context with an instance of the API client

with meli.ApiClient() as api_client:
# Create an instance of the API class
    api_instance = meli.OAuth20Api(api_client)
    grant_type = 'authorization_code' # str
    client_id = '7480524387124622' # Your client_id
    client_secret = 'T2NFwv5Ra2cnWEEy3jRxh2OBEXlJfSu4' # Your client_secret
    redirect_uri = 'http://localhost:5001/login' # Your redirect_uri
    code = 'TG-5fca393b9b1a0c0006a746f5-220566622' # The parameter CODE
    refresh_token = '' # Your refresh_token
try:
    # Request Access Token
    api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuth20Api->get_token: %s\n" % e)

# # Enter a context with an instance of the API client
# with meli.ApiClient() as api_client:
#     # Create an instance of the API class
#     api_instance = meli.RestClientApi(api_client)
#     resource = '/users/MLC564078057/items/search?access_token=APP_USR-7480524387124622-112720-cf4893e5afda5ecd713429535e904e07-220566622' # A resource example like items, search, category, etc.
#     access_token = 'APP_USR-7480524387124622-112720-cf4893e5afda5ecd713429535e904e07-220566622' # Your access token.
#
# try:
#     # Resource path GET
#     api_response = api_instance.resource_get(resource, access_token)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling RestClientApi->resource_get: %s\n" % e)