from locale import currency
from operator import inv
import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *
import json

url = "https://piyush1108.myshopify.com/admin/api/2022-07/orders.json?status=any&created_at_min=2022-10-17"


headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": "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"
}
r = requests.get(url, headers=headers)

invoice = r.json()
loopvar=invoice["orders"]
print("amarnnnnnnnnnnnnnnn")
# print(invoice)
invoicedata={}
for val in loopvar:
    currency1=val["current_subtotal_price_set"]['shop_money']['currency_code']
    odnum=val['order_number']
    cdate=val['created_at']
    dueDate=val['payment_terms']['payment_schedules'][0]['due_at']
    customerid=val['customer']['id']
    gstnote=val['customer']['note']
    gstnote1=gstnote[-15:]
    supply_name=val['customer']["default_address"]["province"]
    bill_address=val['billing_address']['address1'] + " "+val['billing_address']['address2']
    city=val['billing_address']['city']
    state=val['customer']["default_address"]["province"]
    Zip=val['customer']["default_address"]["zip"]
    country1=val['billing_address']['country']
    shipp_address=val['shipping_address']["address1"] +" "+ val['shipping_address']["address2"]
    shipp_city=val['shipping_address']["city"]
    shipp_state=val['shipping_address']["province"]
    shipp_zip=val['shipping_address']["zip"]
    shipp_country=val['shipping_address']["country"]
    total_price=val['total_price']
    lineitem_var = val['line_items']
    final_item_list = []
    for ele in lineitem_var:
        item_code = ele['product_id']
        item_dict = {
        "saleType": "Normal",
        "inventoryType": "INVTP",
        "itemCode": ele['product_id'],
        "itemName": ele['title'],
        "txnQtyAllocationData": {
            "txnQtyAllocationList": [
                {    
                    "batchNo":None,
                    "quantityAttribute": {
                        "inventoryQuantityAttributeOptionList": [
                            {
                                "attributeOptionName": "Normal"
                            }
                        ]
                    },
                    "quantitySerial":None,
                    "quantity":ele['quantity'],
                    "unitPrice":ele['price'],
                }
                
            ]
        },
        "description": "SAMSUNG F62 8GB 128GB Laser Grey",
        "gstRate":"18",
        "discount": ele['total_discount'],        
        "addDiscount": "",       
        "hsnSac":None,
        "type": "Goods",
        "unitName":None,
        "accountName": "Sale of Goods",}
        final_item_list.append(item_dict)
        item_code=val['line_items'][0]['product_id']
        item_title=val['line_items'][0]['title']
        item_variant=val['line_items'][0]['variant_title']
        item_quantity=val['line_items'][0]['quantity']
        item_price=val['line_items'][0]['price']
        items=val['line_items'][0]['tax_lines']
        # print(final_item_list) 
        print("hi khalid here")
        # print( ele['discount_allocations'])
        # print(len(ele['discount_allocations']))
        discount1=None
        discountadd=None
        if len(ele['discount_allocations'])==2:
            discount1=ele['discount_allocations'][0]['amount_set']['shop_money']['amount']
            discountadd=ele['discount_allocations'][1]['amount_set']['shop_money']['amount']


        elif len(ele['discount_allocations'])==1:
            discount1=ele['discount_allocations'][0]['amount_set']['shop_money']['amount']
            discountadd=0

        else:
            discount1=0
            discountadd=0


    

        print(discount1)
        print(discountadd)



        
        
        


        invoicedata={"currencyCode":currency1,"number":odnum,"date":cdate,"dueDate":dueDate,"contactCode":customerid,"customerGstin":gstnote1,"placeSupplyName":supply_name,"address1":bill_address,"city":city,"state":state,"zip":Zip,"country":country1,"shipaddress1":shipp_address,"city1":shipp_city,"state1":shipp_state,"zip1":shipp_zip, "country1":shipp_country,"totalamount":total_price, "itemCode":item_code,"itemName":item_title,"attributeOptionName":item_variant,"quantity":item_quantity,"unitPrice":item_price,"taxlines":items,"line_items_list":final_item_list}
        # print(invoicedata)
        # print("REACHED POST")

        add_item =  {"invoiceList":[
        {
            "taxType":"ETAX",
            "currencyCode":invoicedata['currencyCode'],
            "companyGstin":"07ASEPQ2123K1Z1",
            "branch":"H.O",
            "Category":"",
            "invoiceType":"R",         
            "number":"1000S",
            "date":invoicedata['date'],
            "dueDate":invoicedata['dueDate'],
            "contactCode":"CON-002",
            "contactName":"PRIYANKA ENTERPRISES", 
            "customerGstin":"07AVIPP6600Q1Z0",
            "placeSupplyName":invoicedata['placeSupplyName'],  
            "billAddress":{
            "address1":invoicedata['address1'],
            "city":invoicedata['city'],
            "state":invoicedata['state'],
            "zip":invoicedata['zip'],
            "country":invoicedata['country'],
            "pan":"",
            "gstin":"",
            "type":"BADR"
            },
            "shipAddress": {
            "address1":invoicedata['shipaddress1'],
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
            "amount":"0",
            "roundingAmount":0,
            "reverseChargeFlag":False,
            "flatDiscountFlag":True,
            "flatAddDiscountFlag":False,
            "flatCessFlag":False,
            "flatSubsidyFlag":False,
            "txnDiscountList":None,
            "lineItems": invoicedata['line_items_list'],
            "typeCode": "SINV",
            "status": "BAPP",
            "gstnType": "B2B",
            }
            ]
            }
    print("End for loop")
    print(add_item)