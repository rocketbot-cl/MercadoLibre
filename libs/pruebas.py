import requests
endpoint = "https://api.mercadolibre.com/users/test_user"
data = {"site_id": "mla"}
headers = {"Authorization": "Bearer APP_USR-7480524387124622-120413-6b7f043ca8d69c0ea189111c0a405b3b-220566622"}

print(requests.post(endpoint, data=data, headers=headers).json())