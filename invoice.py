from locale import currency
from operator import inv
import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *
import json


url = "https://piyush1108.myshopify.com/admin/api/2022-07/orders.json?status=any"


headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": "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"
}

# print(headers)
r = requests.get(url, headers=headers)
# print("Accounting Json :- ",r.json())

invoice = r.json()
print(invoice)

currency1 = invoice["orders"][0]["current_subtotal_price_set"]['shop_money']['currency_code']
odnum = invoice["orders"][0]['order_number']
cdate = invoice["orders"][0]['created_at']
dueDate = invoice["orders"][0]['payment_terms']['payment_schedules'][0]['due_at']
customerid = invoice["orders"][0]['customer']['id']
gstnote = invoice["orders"][0]['customer']['note']
gstnote1 = gstnote[-15:]
supply_name = invoice["orders"][0]['customer']["default_address"]["province"]
bill_address = invoice["orders"][0]['billing_address']['address1'] + \
    " "+invoice["orders"][0]['billing_address']['address2']
city = invoice["orders"][0]['billing_address']['city']
state = invoice["orders"][0]['customer']["default_address"]["province"]
zip = invoice["orders"][0]['customer']["default_address"]["zip"]
country1 = invoice["orders"][0]['billing_address']['country']


shipp_address = invoice["orders"][0]['shipping_address']["address1"] + \
    " " + invoice["orders"][0]['shipping_address']["address2"]
shipp_city = invoice["orders"][0]['shipping_address']["city"]
shipp_state = invoice["orders"][0]['shipping_address']["province"]
shipp_zip = invoice["orders"][0]['shipping_address']["zip"]
shipp_country = invoice["orders"][0]['shipping_address']["country"]

total_price = invoice["orders"][0]['total_price']
item_code = invoice["orders"][0]['line_items'][0]['product_id']
item_title = invoice["orders"][0]['line_items'][0]['title']
item_variant = invoice["orders"][0]['line_items'][0]['variant_title']
item_quantity = invoice["orders"][0]['line_items'][0]['quantity']
item_price = invoice["orders"][0]['line_items'][0]['price']
gstrate = invoice["orders"][0]['line_items'][0]['tax_lines'][0]['rate']*100
discount1 = invoice["orders"][0]['line_items'][0]['discount_allocations']
goods=invoice["orders"][0]['line_items'][0]
print(goods)

print(item_price)
print(invoice)
print(gstnote1)


invoicedata = {}
for val in invoice:
    currency1 = invoice["orders"][0]["current_subtotal_price_set"]['shop_money']['currency_code']
    odnum = invoice["orders"][0]['order_number']
    cdate = invoice["orders"][0]['created_at']
    dueDate = invoice["orders"][0]['payment_terms']['payment_schedules'][0]['due_at']
    customerid = invoice["orders"][0]['customer']['id']
    gstnote = invoice["orders"][0]['customer']['note']
    gstnote1 = gstnote[-15:]
    supply_name = invoice["orders"][0]['customer']["default_address"]["province"]
    bill_address = invoice["orders"][0]['billing_address']['address1'] + \
        " "+invoice["orders"][0]['billing_address']['address2']
    city = invoice["orders"][0]['billing_address']['city']
    state = invoice["orders"][0]['customer']["default_address"]["province"]
    zip = invoice["orders"][0]['customer']["default_address"]["zip"]
    country1 = invoice["orders"][0]['billing_address']['country']
    shipp_address = invoice["orders"][0]['shipping_address']["address1"] + \
" " + invoice["orders"][0]['shipping_address']["address2"]
    shipp_city = invoice["orders"][0]['shipping_address']["city"]
    shipp_state = invoice["orders"][0]['shipping_address']["province"]
    shipp_zip = invoice["orders"][0]['shipping_address']["zip"]
    shipp_country = invoice["orders"][0]['shipping_address']["country"]
    total_price = invoice["orders"][0]['total_price']
    item_code = invoice["orders"][0]['line_items'][0]['product_id']
    item_title = invoice["orders"][0]['line_items'][0]['title']
    item_variant = invoice["orders"][0]['line_items'][0]['variant_title']
    item_quantity = invoice["orders"][0]['line_items'][0]['quantity']
    item_price = invoice["orders"][0]['line_items'][0]['price']
    items = invoice["orders"][0]['line_items'][0]['tax_lines']

    invoicedata = {"currencyCode": currency1, "number": odnum, "date": cdate, "dueDate": dueDate, "contactCode": customerid, "customerGstin": gstnote1, "placeSupplyName": supply_name, "address1": bill_address, "city": city, "state": state, "zip": zip, "country": country1, "shipaddress1": shipp_address,"city1": shipp_city, "state1": shipp_state, "zip1": shipp_zip, "country1": shipp_country, "totalamount": total_price, "itemCode": item_code, "itemName": item_title, "attributeOptionName": item_variant, "quantity": item_quantity, "unitPrice": item_price, "taxlines": items}


# print(invoicedata)


data1 = {
    "invoiceList": [
        {
            "taxType": "ETAX",
            "currencyCode": invoicedata['currencyCode'],
            "companyGstin":invoicedata['customerGstin'],
            "branch":"H.O",
            "Category":"",
            "invoiceType":"R",  # If GSTIN than “R” else ‘NA”
            "number":invoicedata['number'],
            "date":invoicedata['date'],
            "dueDate":invoicedata['dueDate'],
            "contactCode":invoicedata['contactCode'],
            "contactName":"PRIYANKA ENTERPRISES",
            # "GSTIN:08AAAAA1234A1Z1" (remove GSTIN: and use only 08AAAAA1234A1Z1)
            "customerGstin":invoicedata['customerGstin'],
            # province (If is null than customer --> default_address --> province)
            "placeSupplyName":invoicedata['placeSupplyName'],
            "billAddress":{
                "address1": invoicedata['address1'],
                "city":invoicedata['city'],
                "state":invoicedata['state'],
                "zip":invoicedata['zip'],
                "country":invoicedata['country'],
                "pan":"",
                "gstin":"",
                "type":"BADR"
            },
            "shipAddress": {
                "address1": invoicedata['shipaddress1'],
                "city":invoicedata['city1'],
                "state":invoicedata['state1'],
                "zip":invoicedata['zip1'],
                "country":invoicedata['country1'],
                "pan":"",
                "gstin":"",
                "type":" SADR "
            },
            "warehouseAddress":None,
            "termCondition":None,
            "customersNotes":None,
            "shippingNumber":None,
            "shippingDate":None,
            "shippingPortCode":None,
            "purchaseOrderNumber":None,
            "purchaseOrderDate":None,
            "buyerOrderNumber":None,
            "buyerOrderDate":None,
            "eWayBillNumber":None,
            "eWayBillDate":None,
            "lRNo":None,
            "otherReference":None,
            "vendorCode":None,
            "vehicleNumber":None,
            "termsOfPayment":None,
            "cin":None,
            "amount":invoicedata['totalamount'],
            "roundingAmount":0,
            "reverseChargeFlag":False,
            "flatDiscountFlag":True,
            "flatAddDiscountFlag":False,
            "flatCessFlag":False,
            "flatSubsidyFlag":False,
            "txnDiscountList":[{

            }
            ],
            "lineItems": [
                {
                    "saleType": "Normal",
                    "inventoryType": "INVTP",
                    "itemCode": invoicedata['itemCode'],
                    "itemName": invoicedata['itemName'],
                    "txnQtyAllocationData": {
                        "txnQtyAllocationList": [
                            {
                                "batchNo": None,
                                "quantityAttribute": {
                                    "inventoryQuantityAttributeOptionList": [
                                     {
                                         # --> variant_title   divide in array by using separator “/”
                                         "attributeOptionName": "Red"
                                     }
                                    ]
                                },
                                "quantitySerial": None,
                                "quantity": invoicedata['quantity'],
                                "unitPrice":invoicedata['unitPrice'],
                            }

                        ]
                    },
                    "description": "SAMSUNG F62 8GB 128GB Laser Grey",
                    "gstRate":  invoicedata['taxlines']*100,
                    # ->line_items-->discount_allocations-->amount (First Item)
                    "discount": "100",
                    # ->line_items-->discount_allocations-->amount (Second item)
                    "addDiscount": "",

                    "hsnSac":None,
                    "type": "Goods",
                    "unitName":None,
                    "accountName": "Sale of Goods",
                }
            ],
            "typeCode": "SINV",
            "status": "BAPP",
            "gstnType": "B2B",
        }
    ]
}

print(data1)