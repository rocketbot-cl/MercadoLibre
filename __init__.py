# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "MercadoLibre" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
"""
    Obtengo el modulo que fue invocado
"""
from MercadoLibre import MercadoLibre
import webbrowser
import json

module = GetParams("module")

global mercado_libre

if module == "setCredentials":
    client_secret = GetParams("client_secret")
    client_id = GetParams("client_id")
    client_id = int(client_id)
    redirect_uri = GetParams("redirect_uri")
    code = GetParams("code")
    access_token = GetParams("access_token")
    credentials_filename = 'credentials.json'
    file_credentials = base_path + "modules" + os.sep + "MercadoLibre" + os.sep + credentials_filename
    try:
        try:
            with open(file_credentials) as json_file:
                data = json.load(json_file)
            refresh_token = data['refresh_token']
            mercado_libre = MercadoLibre(client_secret, redirect_uri, client_id, code, refresh_token=refresh_token)
            grant_type = 'refresh_token'
            mercado_libre.get_access_token(file_credentials, grant_type=grant_type)
        except IOError:
            mercado_libre = MercadoLibre(client_secret, redirect_uri, client_id, code)
            mercado_libre.get_access_token(file_credentials)
        # if mercado_libre.access_token == '':
        #     access_token_new = mercado_libre.get_access_token()
        #     SetVar(access_token, access_token_new)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "getCode":
    client_id = GetParams("client_id")
    redirect_uri = GetParams("redirect_uri")
    try:
        url_code = "https://auth.mercadolibre.com/authorization?response_type=code&client_id={}&redirect_uri={}".format(
            client_id, redirect_uri)
        webbrowser.open(url_code, new=2)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "searchAllOrders":
    result = GetParams("result")
    filter = GetParams("filter")
    try:
        resource = "orders/search?seller=" + str(mercado_libre.user_id)
        if filter:
            resource = resource + "&order.status=paid&sort={}".format(filter)
        api_response = mercado_libre.get_resource(resource)
        SetVar(result, api_response)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "uploadInvoice":
    pack_id = str(GetParams("pack_id"))
    invoice_path = GetParams("invoice_path")
    try:
        mercado_libre.upload_invoice(pack_id, invoice_path)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "getShippingDetail":
    shipping_id = GetParams("shipping_id")
    result = GetParams("result")
    try:
        resource_shipping = "shipments/" + shipping_id
        shipping_details = mercado_libre.get_resource(resource_shipping)
        SetVar(result, shipping_details)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e