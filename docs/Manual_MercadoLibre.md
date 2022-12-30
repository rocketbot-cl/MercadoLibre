# MercadoLibre
  
Module to work with MercadoLibre functions in Rocketbot  

*Read this in other languages: [English](Manual_MercadoLibre.md), [Español](Manual_MercadoLibre.es.md).*
  
![banner](imgs/Banner_Mercadolibre.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Set credentials
  
Set credentials to make available the API
|Parameters|Description|example|
| --- | --- | --- |
|client_id|client_id of MercadoLibre|Your client_id|
|client_secret|client_secret of MercadoLibre|Your client_secret|
|redirect_uri|redirect_uri of MercadoLibre|htpps://mercadolibre.cl/|
|code|code of MercadoLibre|TG-9999999999999999999999|

### Get code
  
Get the code to work with the API
|Parameters|Description|example|
| --- | --- | --- |
|client_id|client_id of the app|Your client_id|
|redirect_uri|redirect_uri of the app|htpps://mercadolibre.cl/|

### Get all orders
  
Get all the orders from the seller
|Parameters|Description|example|
| --- | --- | --- |
|Filter|Order filter|Filter|
|Result|Variable where the result will be saved|result|

### Upload invoice
  
Upload invoice
|Parameters|Description|example|
| --- | --- | --- |
|PACK_ID|Value of PACK_ID of the order|PACK_ID or ORDER_ID|
|Invoice path|Invoice path to upload|Path|

### Get shipping details
  
Get shipping details
|Parameters|Description|example|
| --- | --- | --- |
|shipping_id|shipping_id of the shipping|shipping_id|
|Result|Variable where the result will be saved|Variable|

### Get billing info
  
Get the information uploaded in an order regarding a buyer's billing data
|Parameters|Description|example|
| --- | --- | --- |
|order_id|order_id of the billing|order_id|
|Result|Variable where the result will be saved|Variable|
