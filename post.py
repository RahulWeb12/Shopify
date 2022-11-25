# ------------------------------------------------------------ POST ------------------------------------------------------------------------------

import shopify
import requests
import json
from shopify.base import ShopifyResource
from shopify.resources import *

API_KEY ='8bb4a94c72ffedf66794f6588cbb9283'
PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
token='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'
API_VERSION='2022-07'


# url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/products.json" % (API_KEY, token)


url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/orders.json" % (API_KEY, token)

# url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/shipping_zones.json" % (API_KEY, token)


# url= 'https://8bb4a94c72ffedf66794f6588cbb9283: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@zia-warehouse.myshopify.com/admin/api/2022-07/products.json'


# add_item = {
#         "product": {
#           "title": "GreekGrapes",
#         }
#       }


add_item = {"order":{"line_items":[{"variant_id":6846907088969,"quantity":1,"price":100,"name":"Fruit seller","title":"hello i am fruit seller"}]}}

headers = {"Accept": "application/json", "Content-Type": "application/json"}

r = requests.post(url, json=add_item,  headers=headers)

print(r.json()) 