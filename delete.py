# -------------------------------------------------------------------------- Delete -------------------------------------------------------------------

import shopify
import requests
import json
from shopify.base import ShopifyResource
from shopify.resources import *

API_KEY ='8bb4a94c72ffedf66794f6588cbb9283'
PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
API_VERSION='2022-07'


url= 'https://8bb4a94c72ffedf66794f6588cbb9283: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@zia-warehouse.myshopify.com/admin/api/2022-07/products.json?fields=6846472192073'

headers = {"Content-Type": "application/json; charset=utf-8"}
  
r = requests.delete(url,headers=headers)

print(r.status_code)

