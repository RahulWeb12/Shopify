# ------------------------------------------------------------ GET ------------------------------------------------------------------------

import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *

API_KEY ='8bb4a94c72ffedf66794f6588cbb9283'
# PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
token='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'

API_VERSION='2022-07'

# url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/products.json?fields=id,images,title" % (API_KEY, token)


# All Shipping find out
url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/shipping_zones.json" % (API_KEY, token)

# url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/products.json" % (API_KEY, token)






# url = 'https://<shopname>.myshopify.com/admin/api/2022-01/products/count.json'
# url = 'https://8bb4a94c72ffedf66794f6588cbb9283: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@zia-warehouse.myshopify.com/admin/api/2022-07/products.json?fields=id,images,title'
header = {
                # 'X-Shopify-Storefront-Access-Token':'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',
                'Content-Type': 'application/json',
                'Authorization': 'Basic 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'
}

r = requests.get(url, headers=header)

# print(r.text)
# -----------------------------------------------------------------------------------------------------------------------------------------

url4 = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/customers.json" % (API_KEY, token)
# url4 = "https://piyush1108.myshopify.com/admin/api/2022-07/"

headers = {
                # 'X-Shopify-Storefront-Access-Token':'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',
                'Content-Type': 'application/json',
                'Authorization': 'Basic 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'
}

r = requests.get(url4, headers=headers)

print(r.json())































# API_KEY ='8bb4a94c72ffedf66794f6588cbb9283'
# PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
# API_VERSION='2022-07'
# shop_url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-01/products/count.json" % (API_KEY, PASSWORD)
# shopify.ShopifyResource.set_site(shop_url)



# shop = shopify.Shop.current


	
# # Create a new product
# new_product = shopify.Product()
# new_product.title = "Burton Custom Freestyle 151"
# new_product.product_type = "Snowboard"
# new_product.vendor = "Burton"
# success = new_product.save() 






# r = requests.get(url, headers=header)

# print(r.text)


# import shopify

# API_KEY ='8bb4a94c72ffedf66794f6588cbb9283'
# PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
# API_VERSION='2022-07'
# SHOP_NAME='zia-warehouse'
# shop_url = "https://%s.myshopify.com/admin" % (SHOP_NAME)
# shopify.ShopifyResource.set_user("API_KEY")
# shopify.ShopifyResource.set_password("PASSWORD")

# #shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, SHOP_NAME, API_VERSION)
# shopify.ShopifyResource.set_site(shop_url)

# # Get the current shopshop = shopify.Shop.current()

# # Get a specific productproduct = shopify.Product.find(1961541795955)

# print(product.title)
