import meli
from meli.rest import ApiException


class MercadoLibre:

    def __init__(self, client_secret, redirect_uri, client_id, code):
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri
        self.CLIENT_ID = client_id
        self.code = code
        self.configuration = meli.Configuration(
            host="https://api.mercadolibre.com"
        )
        self.access_token = None
        self.refresh_token = ''
        self.user_id = None

    def get_access_token(self, grant_type='authorization_code'):

        with meli.ApiClient() as client:
            api_instance = meli.OAuth20Api(client)
            client_id = self.CLIENT_ID  # Your client_id
            client_secret = self.CLIENT_SECRET  # Your client_secret
            redirect_uri = self.REDIRECT_URI  # Your redirect_uri
            code = self.code  # The parameter CODE
            refresh_token = self.refresh_token  # Your refresh_token
        try:
            # Request Access Token
            api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id,
                                                  client_secret=client_secret, redirect_uri=redirect_uri, code=code,
                                                  refresh_token=refresh_token)
            self.access_token = api_response["access_token"]
            self.refresh_token = api_response["refresh_token"]
            self.user_id = api_response["user_id"]
            print(api_response)
            return api_response
        except ApiException as exception:
            print(f"Exception when calling OAuth20Api->get_token: {exception}\n")

    def get_resource(self, resource):
        # Enter a context with an instance of the API client
        if self.access_token is None:
            raise Exception("Access token has not been generated ")

        with meli.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = meli.RestClientApi(api_client)
            access_token = self.access_token  # Your access token.

        try:
            # Resource path GET
            print(resource)
            api_response = api_instance.resource_get(resource, access_token)
            results = api_response
            print(results)
        except ApiException as e:
            print("Exception when calling RestClientApi->resource_get: %s\n" % e)


if __name__ == '__main__':
    APP_ID = 7480524387124622
    CLIENT_SECRET = 'T2NFwv5Ra2cnWEEy3jRxh2OBEXlJfSu4'
    REDIRECT_URI = "http://localhost:5001/login"
    CODE = 'TG-5fce383f738cf10006c5ef33-386738209'
    access_token = "APP_USR-7480524387124622-120714-e0545839d47e481354196a1ed64c39e5-386738209"

    ml = MercadoLibre(CLIENT_SECRET, REDIRECT_URI, APP_ID, CODE)
    # ml.get_access_token()
    ml.access_token = access_token
    ml.get_resource("users/me")
