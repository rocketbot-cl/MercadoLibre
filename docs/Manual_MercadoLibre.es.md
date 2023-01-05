# MercadoLibre
  
Módulo para trabajar con las funciones de MercadoLibre en Rocketbot  

*Read this in other languages: [English](Manual_MercadoLibre.md), [Español](Manual_MercadoLibre.es.md).*
  
![banner](imgs/Banner_Mercadolibre.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Establecer credenciales
  
Establece las credenciales para tener disponible la API
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|client_id|client_id de MercadoLibre|Your client_id|
|client_secret|client_secret de MercadoLibre|Your client_secret|
|redirect_uri|redirect_uri de MercadoLibre|htpps://mercadolibre.cl/|
|code|code de MercadoLibre|TG-9999999999999999999999|

### Obtener codigo
  
Obtiene el codigo para trabajar con la API
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|client_id|client_id de la app|Your client_id|
|redirect_uri|redirect_uri de la app|htpps://mercadolibre.cl/|

### Obtener todas las ordenes
  
Obtiene todas las ordenes del comprador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Filtro de ordenes|Filtro|
|Resultado|Variable donde se guardará el resultado|result|

### Subir factura
  
Asocia una factura a una orden
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|PACK_ID|Valor de PACK_ID de la orden|PACK_ID or ORDER_ID|
|Ruta de la factura|Ruta de la factura a subir|Ruta|

### Obtener detalles de envio
  
Obtiene los detalles del envio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|shipping_id|shipping_id del envio|shipping_id|
|Resultado|Variable donde se guardara el resultado|Variable|

### Obtener datos de facturacion
  
Para obtener la información cargada en una orden respecto de los datos de facturación de un comprador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|order_id|order_id de la factura|order_id|
|Resultado|Variable donde se guardará el resultado|Variable|
