from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
import webbrowser


# Defining the host, defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)

class MercadoLibre:
    USER_ID = 386738209
    APP_ID = 7480524387124622
    CLIENT_SECRET = 'T2NFwv5Ra2cnWEEy3jRxh2OBEXlJfSu4'
    REDIRECT_URI = "http://localhost:5001/login"
    CODE = 'TG-5fca6192004135000646c518-386738209'
    ACCESS_TOKEN = 'APP_USR-7480524387124622-120416-99415cd9b0bb1d00eb67553dce67a5f8-386738209'
    SELLER_ID = 386738209
"""
 Get Code: https://auth.mercadolibre.com/authorization?response_type=code&client_id={APP_ID}&redirect_uri={REDIRECT_URI}
"""


ml = MercadoLibre()

def get_code(client_id, redirect_uri):
    url_code = "https://auth.mercadolibre.com/authorization?response_type=code&client_id="+client_id+"&redirect_uri="+redirect_uri
    webbrowser.open(url_code, new=2)
    

def get_access_token():
    # Enter a context with an instance of the API client
    with meli.ApiClient() as api_client:
    # Create an instance of the API class
        api_instance = meli.OAuth20Api(api_client)
        grant_type = 'authorization_code' # str
        client_id = ml.APP_ID # Your client_id
        client_secret = ml.CLIENT_SECRET # Your client_secret
        redirect_uri = 'http://localhost:5001/login' # Your redirect_uri
        code = ml.CODE # The parameter CODE
        refresh_token = '' # Your refresh_token

    try:
        # Request Access Token
        api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OAuth20Api->get_token: %s\n" % e)


def get_resource(resource_str):
    # Enter a context with an instance of the API client
    with meli.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = meli.RestClientApi(api_client)
        resource = resource_str # A resource example like items, search, category, etc.
        access_token = ml.ACCESS_TOKEN # Your access token.

    try:
        # Resource path GET
        print(resource)
        api_response = api_instance.resource_get(resource, access_token)
        results = api_response["results"]
        pprint(results)
    except ApiException as e:
        print("Exception when calling RestClientApi->resource_get: %s\n" % e)


if __name__ == "__main__":

    resource = {
        "get_orders":"orders/search?seller="
    }
    #MLC564078057
    get_resource(resource["get_orders"] + str(ml.SELLER_ID))
    # get_access_token()