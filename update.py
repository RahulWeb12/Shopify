# -------------------------------------------------------- PUT -------------------------------------------------------------------

import shopify
import requests
import json
from shopify.base import ShopifyResource
from shopify.resources import *

API_KEY ='8bb4a94c72ffedf66794f6588cbb9283'
PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
API_VERSION='2022-07'


url= 'https://8bb4a94c72ffedf66794f6588cbb9283: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@zia-warehouse.myshopify.com/admin/api/2022-07/products.json'

headers = {"Content-Type": "application/json; charset=utf-8"}

payload = {
        "product": {
          "title": "Kiwi",
          "body_html": "The kiwifruit, or Chinese gooseberry, originally grew wild in China.",
        }
      }

headers = {"Accept": "application/json", "Content-Type": "application/json"}

r = requests.put(url, json=payload,  headers=headers)

print(r.json())

# --------------------------------------------------------------------------------------------------
