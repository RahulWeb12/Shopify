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

# Particular Quantity Checks
url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/products/6846907088969.json" % (API_KEY, token)




# add_item = {"order":{"line_items":[{"variant_id":6846907088969,"quantity":1,"price":100,"name":"Fruit seller","title":"hello i am fruit seller"}]}}

headers = {"Accept": "application/json", "Content-Type": "application/json"}

r = requests.get(url, headers=headers)


item=r.json()

# print(item)


value=item['product']['variants'][0]['inventory_quantity']


print("Quantity :- ",value,"\n")

qty=1

try:
    if qty <= value:
        print("Product is available")
    else:
        print("Please lower the quantity ")
except:
    print("Out of Stocks")

























# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# All Shipping find out
# url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/shipping_zones.json" % (API_KEY, token)

# header = {
#                 # 'X-Shopify-Storefront-Access-Token':'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',
#                 'Content-Type': 'application/json',
#                 'Authorization': 'Basic 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'
#     }

# r = requests.get(url, headers=header)

# print(r.text)