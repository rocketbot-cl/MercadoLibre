from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)


# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meli.ItemsApi(api_client)
    id = '564078057' # str |

    try:
        # Return a Item.
        api_response = api_instance.items_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ItemsApi->items_id_get: %s\n" % e)