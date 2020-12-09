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
import json
from MercadoLibre import MercadoLibre


base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "MercadoLibre" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

global mercado_libre

if module == "setCredentials":
    client_secret = GetParams("client_secret")
    client_id = GetParams("client_id")
    redirect_uri = GetParams("redirect_uri")
    code = GetParams("code")

    mercado_libre = MercadoLibre(client_secret, redirect_uri, client_id, code)
    if mercado_libre.access_token is None:
        mercado_libre.get_access_token()
