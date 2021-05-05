import meli
from meli.rest import ApiException
import json
import requests
from requests.structures import CaseInsensitiveDict
import os
from pathlib import Path


class MercadoLibre:

    def __init__(self, client_secret, redirect_uri, client_id, code, access_token='', refresh_token=''):
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri
        self.CLIENT_ID = client_id
        self.code = code
        self.configuration = meli.Configuration(
            host="https://api.mercadolibre.com"
        )
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.user_id = None

    def get_access_token(self, file_credentials,grant_type='authorization_code'):

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
            self.write_credentials(api_response, file_credentials)
            print(api_response)
            return api_response
            # print()
        except ApiException as exception:
            print(f"Exception when calling OAuth20Api->get_token: {exception}\n")

    def get_refresh_token(self):
        print()

    def write_credentials(self, credentials, file_credentials):
        with open(file_credentials, 'w') as outfile:
            json.dump(credentials, outfile)

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
            return results
        except ApiException as e:
            print("Exception when calling RestClientApi->resource_get: %s\n" % e)

    def upload_invoice(self, pack_id, path_file):
        # pack_id = 4208464169
        url = "https://api.mercadolibre.com/packs/{pack_id}/fiscal_documents".format(pack_id=pack_id)
        headers = CaseInsensitiveDict()
        # access_token = 'APP_USR-7480524387124622-010713-4f28098e6276386b2220a0e4c0130897-386738209'
        headers["Authorization"] = "Bearer {access_token}".format(access_token=self.access_token)
        files = {'fiscal_document': open(path_file, 'rb')}
        resp = requests.post(url, files=files, headers=headers)
        print(resp.text)