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

module = GetParams("module")

global mercado_libre

if module == "setCredentials":
    client_secret = GetParams("client_secret")
    client_id = GetParams("client_id")
    client_id = int(client_id)
    redirect_uri = GetParams("redirect_uri")
    code = GetParams("code")
    try:
        mercado_libre = MercadoLibre(client_secret, redirect_uri, client_id, code)
        if mercado_libre.access_token is None:
            mercado_libre.get_access_token()
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

