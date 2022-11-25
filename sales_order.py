from locale import currency
from operator import inv
import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *
import json
import datetime as dt
from datetime import datetime


global all_data 

#  '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'

global value
global value_preserve_key
# ---------------------- Accounting Login -----------------------------------------
url1 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/login"
add_item = {
    # "username": "ashish.baranwal@hostbooks.com",
    # "password":  "12345678"
    "username": "piyushqa2018a@gmail.com",
    "password":  "test@123"
}
r = requests.post(url1, json=add_item)
token = r.json()

value = token['data']['user']['accessToken']
value_preserve_key = token['data']['user']['preserveKey']

# x-company
# companyUUID

url2 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/companies"
headers = {
    'x-auth-token': value,
    "x-version": "IND"
}

print("I am waiting..........")
r = requests.get(url2, headers=headers)
print("***********************************")
token2 = r.json()
companyUID = token2["data"]["comapanies"][0]["companyUID"]
# print("companyUID :- ", companyUID)

print(" The wait is over.....")

url3 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/validateUserLogin"
headers = {
    "x-version": "IND",
    "x-preserveKey":  value_preserve_key,
    # "x-company":  "F941FF61-7FAA-DD71-919B-1AE3F013013E",
    "x-company":  "389B7CCF-2F78-AC7B-ECD8-87FDEDE3E083",
    # "x-company":  companyUID,
    "x-forwarded-portal":  "true",
    "Content-Type": "application/json"
}
r = requests.get(url3, headers=headers)
print("***************************************************")
token3 = r.json()

# print(token3)

# x_company=token2["data"]["comapanies"][0]["companyUID"]
print("####################################################")

request_type_name = "GET"
response_type_name = "SUCCESS"
record_category_name = "ACCOUNTING LOGIN"
date_time_data = datetime.today().isoformat()
# print("Today's date:", date_time_data)


url = "https://piyush1108.myshopify.com/admin/api/2022-07/orders.json?status=any&created_at_min=2022-10-17"

# url = "https://%s.myshopify.com/admin/api/2022-07/orders.json?status=any" % (storename1)

headers = {"Content-Type": "application/json",
           "X-Shopify-Access-Token": "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"
           }

r = requests.get(url, headers=headers)
invoice = r.json()
loopvar = invoice["orders"]
now = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
batch = ('HB/'+now.strftime("%d""%m""%y""%H""%M""%S"))
print(batch)
suc = 0
fail = 0
invoicedata = {}

print("Loopvar--------------------------------",len(loopvar))
for val in loopvar:
    currency1 = val["current_subtotal_price_set"]['shop_money']['currency_code']
    odnum = val['order_number']
    cdate = val['created_at']
    dueDate = val['payment_terms']['payment_schedules'][0]['due_at']
    customerid = val['customer']['id']
    gstnote = val['customer']['note']
    print("gstnote :- ",gstnote)
    gstntype = None
    invoicetype = None
    if len(gstnote) == 0:
        print("length if started.................")
        gstntype = "B2C"
        invoicetype = "NA"

    else:
        gstntype = "B2B"
        invoicetype = "R"
        gstnote1 = gstnote[-15:]
        supply_name = val['customer']["default_address"]["province"]
        bill_address = val['billing_address']['address1'] + \
            " "+val['billing_address']['address2']
        city = val['billing_address']['city']
        state = val['customer']["default_address"]["province"]
        Zip = val['customer']["default_address"]["zip"]
        country1 = val['billing_address']['country']
        shipp_address = val['shipping_address']["address1"] + \
            " " + val['shipping_address']["address2"]
        shipp_city = val['shipping_address']["city"]
        shipp_state = val['shipping_address']["province"]
        shipp_zip = val['shipping_address']["zip"]
        shipp_country = val['shipping_address']["country"]
        total_price = val['total_price']
        lineitem_var = val['line_items']
        gstrate = (val['line_items'][0]['tax_lines'][0]['rate'])*100
        print("gstrate :-",gstrate)
        final_item_list = []
        print("Else For Loop ")
        for ele in lineitem_var:
            item_code = ele['product_id']
            finaldiscount1 = float(0)
            finaldiscountadd = float(0)
            finalqty = float(ele['quantity'])
            # print(finalqty)
            # print('hi kalash is here ')
            lendis = len(ele['discount_allocations'])
            if lendis == 2:
                # print("i have entered in len2 condition ")
                finaldiscount1 = float(
                    ele['discount_allocations'][0]['amount'])
                # print(finaldiscount1)
                finaldiscount1 = finaldiscount1/finalqty
                # print(finaldiscount1)
                finaldiscountadd = float(
                    ele['discount_allocations'][1]['amount'])
                finaldiscountadd = finaldiscountadd/finalqty
            elif lendis == 1:
                # print("i have entered in len1 condition ")
                finaldiscount1 = float(
                    ele['discount_allocations'][0]['amount'])
                finaldiscount1 = finaldiscount1/finalqty
                finaldiscountadd = float(0)

            attoption = []
            aatvar = (ele['variant_title'].replace(" ", "")).split('/')
            # print(aatvar)
            norobj = {"attributeOptionName": aatvar[0]}
            attoption.append(norobj)
            colobj = {"attributeOptionName": aatvar[1]}
            attoption.append(colobj)

            item_dict = {
                "saleType": "Normal",
                "inventoryType": "INVTP",
                "itemCode": None,
                "itemName": ele['title'],
                "txnQtyAllocationData": {
                    "txnQtyAllocationList": [
                        {
                            "batchNo": None,
                            "quantityAttribute": {
                                "inventoryQuantityAttributeOptionList": attoption
                            },
                            "quantitySerial": None,
                            "quantity": ele['quantity'],
                            "unitPrice":ele['price'],
                        }

                    ]
                },
                "description": "SAMSUNG F62 8GB 128GB Laser Grey",
                "gstRate": gstrate,
                "discount": finaldiscount1,
                "addDiscount": round(finaldiscountadd, 0),

                "hsnSac": None,
                "type": "Goods",
                "unitName": None,
                "accountName": "Sale of Goods", }
            final_item_list.append(item_dict)

            print("Second For End")

        item_code = val['line_items'][0]['product_id']
        item_title = val['line_items'][0]['title']
        item_variant = val['line_items'][0]['variant_title']
        item_quantity = val['line_items'][0]['quantity']
        item_price = val['line_items'][0]['price']
        items = val['line_items'][0]['tax_lines']
        print("hi khalid here")
        shipline = val['shipping_lines']
        if len(shipline) != 0:
            for k in shipline:
                shipprice = k['price']
                shiptitle = k['title']
                shipdict = {
                    "saleType": "Normal",
                    "inventoryType": "INVTS",
                    "itemCode": None,
                    "itemName": None,
                    "txnQtyAllocationData":  None,
                    "quantity": 1,
                    "unitPrice": shipprice,
                    "description": shiptitle,
                    "gstRate": 0,
                    "discount": 0,
                    "addDiscount": 0,
                    "hsnSac": None,
                    "type": "Service",
                    "unitName": None,
                    "accountName": "Sale of Goods"
                }
                final_item_list.append(shipdict)
        invoicedata = {"currencyCode": currency1, "number": odnum, "date": cdate, "dueDate": dueDate, "contactCode": customerid, "customerGstin": gstnote1, "placeSupplyName": supply_name, "address1": bill_address, "city": city, "state": state, "zip": Zip, "country": country1, "shipaddress1": shipp_address,
                       "city1": shipp_city, "state1": shipp_state, "zip1": shipp_zip, "country1": shipp_country, "totalamount": total_price, "itemCode": item_code, "itemName": item_title, "attributeOptionName": item_variant, "quantity": item_quantity, "unitPrice": item_price, "taxlines": items, "line_items_list": final_item_list}
        # print(invoicedata)
        print("REACHED POST")
        di = invoicedata['dueDate']
        x = di.split('T')[0].split('-')
        pidate = x[2]+"-"+x[1]+"-"+x[0]
        dddate = invoicedata['date']
        y = dddate.split('T')[0].split('-')
        oidate = y[2]+"-"+y[1]+"-"+y[0]
        # ---------------------------------- Post Data On Accounting------------------------------------

        url4 = "https://sandboxin2accounts.hostbooks.in/hostbook/api/transaction/add"

        url_header = {
            "Content-Type": "application/json",
            "x-auth-token": value,
            "x-preserveKey":  value_preserve_key,
            # dynamics
            # "x-company": "F941FF61-7FAA-DD71-919B-1AE3F013013E"
            "x-company": "389B7CCF-2F78-AC7B-ECD8-87FDEDE3E083",
            # "x-company": companyUID
        }
        print("Url Header Post Data On ACCOUNTING :- ", url_header)
        add_item = {"salesOrderList": [
            {
                "taxType": "ETAX",
                "currencyCode": invoicedata['currencyCode'],
                "companyGstin":"29AADCK7940H000",
                "branch":"H.O",
                "Category":"",
                "invoiceType":invoicetype,
                "number":invoicedata['number'],
                "date":oidate,
                "expiryDate":pidate,
                "contactCode":invoicedata['contactCode'],
                "contactName":"PRIYANKA ENTERPRISES",
                "customerGstin":"29AADCK7940H000",
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
                "flatAddDiscountFlag":True,
                "flatCessFlag":False,
                "flatSubsidyFlag":False,
                "txnDiscountList":None,
                "lineItems": invoicedata['line_items_list'],
                "typeCode": "SINV",
                "status": "SODT",
                "gstnType": gstntype,
            }
        ]
        }

        r = requests.post(url4, json=add_item,  headers=url_header)
        print(r.json())
        res1 = r.json()['message']
        if (r.json()['fieldErrors'] == None):
            res2 = "Done"
        else:
            res2 = r.json()['fieldErrors'][0]['message'].split('.')[0]
        print("End for loop")
        if (r.json()['status'] == 200):
            statusmsg = "SUCCESS"
            suc += 1
        else:
            statusmsg = "FAILED"
            fail += 1
        status = statusmsg
        remark = res2
        module_type = "Sales Order"
        so_no = invoicedata['number']
        amount = invoicedata['totalamount']
        date = oidate
        customer = invoicedata['contactCode']
        print(add_item)
        print("  after sales order save")

    print(" i am in Try")
    request_type_name = "POST"
    response_type_name = "SUCCESS"
    record_category_name = "SALES ORDER SYNC"
    date_time_data = datetime.today().isoformat()
    # print("Today's date:", date_time_data)
    tot = suc+fail
    modulesync = "Sales Order"
    now = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
    cdate = now.strftime("%d"+"/"+"%m"+"/"+"%y" + " "+"%H"+":"+"%M"+":"+"%S")
    totalrecordscus = tot
    successcus = suc
    failcus = fail
    status1 = ""
    if failcus == 0:
        status1 = "SUCCESS"
    elif successcus == 0:
        status1 = "FAILED"
    else:
        status1 = "PARTIALLY"+" "+"SUCCESS"
   
    res1 = r.json()['message']
    if res1 == "Batch Data Added successfully":
        print("Data Post Success fully.........")
    else:
        print("Data Post not Sucess fully !!!!!!!!!!1")
