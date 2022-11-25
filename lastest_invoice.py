from locale import currency
from operator import inv
import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *
import datetime as dt
import json
from datetime import datetime

global all_data
token1 = "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"
global storename
storename = "gcl-ecommerce"
print(token1)
global value
global value_preserve_key

date_time_data = datetime.today().isoformat()
print("Today's date:", date_time_data)
url = "https://%s.myshopify.com/admin/api/2022-07/orders.json?status=any/" % (storename)
headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": token1
            }

r = requests.get(url, headers=headers)
invoice = r.json()
loopvar = invoice["orders"]
print("amarnnnnnnnnnnnnnnn")
suc = 0
fail = 0
now = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
batch = ('HB/'+now.strftime("%d""%m""%y""%H""%M""%S"))
invoicedata = {}
try:
    print(len(loopvar))
    for val in loopvar:
        # print(val)
        currency1 = val["current_subtotal_price_set"]['shop_money']['currency_code']
        print("Currency code", currency1)
        odnum = val['order_number']
        print("Order number  :-", odnum)
        cdate = val['created_at']
        print("cdate :-", cdate)
        if(val['payment_terms'] != None):
            dueDate = val['payment_terms']['payment_schedules'][0]['due_at']           #payment term not None
        else:
            dueDate=None
        customerid = val['customer']['id']
        print("customerid :-", customerid)

        gstnote = val['customer']['note']
        print("gstnote :-", gstnote)                 #Gstin is None 
        if(gstnote != None):
            gstnote1 = gstnote[-15:]
        else:
            gstnote1=None 
        gstntype = None
        invoicetype = None
        if gstnote == None:
            gstntype = "B2C"
            invoicetype = "NA"
        else:
            stntype = "B2B"
            invoicetype = "R"
        # gstnote1 = gstnote[-15:]                             not able to fillter gst number Gst number is None
        print("GSTN", gstnote)
        supply_name = val['customer']["default_address"]["province"]
        print("supply_name :-", supply_name)
        add1=val['billing_address']['address1'] 
        add2=val['billing_address']['address2'] 
        bill_address = add1+add2
        print("billing_address :- ", bill_address)

        city = val['billing_address']['city']
        print("city :-", city)
        state = val['customer']["default_address"]["province"]
        print("state :-", state)

        Zip = val['customer']["default_address"]["zip"]
        print("Zip :- ",Zip)
        country1 = val['billing_address']['country']
        print("country",country1)
        shipp_address = val['shipping_address']["address1"] +" " + val['shipping_address']["address2"]
        print("Shipp_address :-",shipp_address)

        shipp_city = val['shipping_address']["city"]
        print("Sipp_City :-",shipp_city)

        shipp_state = val['shipping_address']["province"]
        print("Shipp_state :- ",shipp_state)

        shipp_zip = val['shipping_address']["zip"]
        print("shipp_zip :-",shipp_zip)
        
        shipp_country = val['shipping_address']["country"]
        print("shipp_country :- ", shipp_country)

        total_price = val['total_price']
        print("total_price :-",total_price)

        lineitem_var = val['line_items']
        print("lineitem_var :-",lineitem_var)

        gstrate = (val['line_items'][0]['tax_lines'][0]['rate'])*100
        print("gstrate :-",gstrate)

        final_item_list = []
        for ele in lineitem_var:
            item_code = ele['product_id']
            finaldiscount1 = float(0)
            
            finaldiscountadd = float(0)
            finalqty = float(ele['quantity'])
            print("final Qty : -", finalqty)
            
            lendis = len(ele['discount_allocations'])
            print("ele :- ",ele['title'])
            print("discount : -", lendis)
            if lendis == 2:
                print("i have entered in len2 condition ")

                finaldiscount1 = float(ele['discount_allocations'][0]['amount'])
                print(finaldiscount1)
                
                finaldiscount1 = finaldiscount1/finalqty
                print(finaldiscount1)
        
                finaldiscountadd = float(ele['discount_allocations'][1]['amount'])
                
                finaldiscountadd = finaldiscountadd/finalqty
            elif lendis == 1:
                print("i have entered in len1 condition ")
                finaldiscount1 = float(ele['discount_allocations'][0]['amount'])
                finaldiscount1 = finaldiscount1/finalqty
                finaldiscountadd = float(0)
            else:
                finaldiscount1=0
                finaldiscountadd=0.00
        # -------------------------------------------------------------------------------------------------
            attoption=[]
            if(ele['variant_title'] != ""):
                aatvar = (ele['variant_title'].replace(" ", "")).split('/')
                print("aatvar :- ",aatvar)

                norobj = {"attributeOptionName": aatvar[0]}                 

                attoption.append(norobj)
                print("attoption :-",attoption)

                colobj = {"attributeOptionName": aatvar[1]}

                attoption.append(colobj)
                print("attoption :-",attoption)
            else:
                pass
        # ----------------------------------------------------------------------------------------------------

            print("finaldiscount :-",finaldiscount1)
            print(finaldiscountadd)
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
                    "addDiscount": round(finaldiscountadd,0),
                    "hsnSac": None,
                    "type": "Goods",
                    "unitName": None,
                    "accountName": "Sale of Goods", 
                }
            final_item_list.append(item_dict)
            print("final_item_list :- ",final_item_list)

            item_code = val['line_items'][0]
            print("item code :- ",item_code)
            

            item_title = val['line_items'][0]['title']
            print("item_title :-",item_title)

            item_variant = val['line_items'][0]['variant_title']
            item_quantity = val['line_items'][0]['quantity']
            item_price = val['line_items'][0]['price']
            items = val['line_items'][0]['tax_lines']
            print("hi khalid here")
            # code by kalash
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
            invoicedata = {"currencyCode": currency1, "number": odnum, "date": cdate, "dueDate":dueDate, "contactCode": customerid,  "customerGstin": gstnote1, "placeSupplyName": supply_name, "address1": bill_address, "city": city, "state": state, "zip":Zip,    "country": country1, "shipaddress1": shipp_address,
                           "city1": shipp_city, "state1": shipp_state, "zip1": shipp_zip, "country1": shipp_country, "totalamount":   total_price, "itemCode": item_code, "itemName": item_title, "attributeOptionName": item_variant, "quantity":  item_quantity, "unitPrice": item_price, "taxlines": items, "line_items_list": final_item_list}
            # print(invoicedata)
            print("REACHED POST")
            du = invoicedata['dueDate']
            x = du.split('T')[0].split('-')
            pdate = x[2]+"-"+x[1]+"-"+x[0]
            # print(pdate)
            ddate = invoicedata['date']
            y = ddate.split('T')[0].split('-')
            odate = y[2]+"-"+y[1]+"-"+y[0]
            print(odate)
            add_item = {"invoiceList": [
                {
                    "taxType": "ETAX",
                    "currencyCode": invoicedata['currencyCode'],
                    "companyGstin":"29AADCK7940H000",
                    "branch":"H.O",
                    "Category":"",
                    "invoiceType":invoicetype,
                    "number":invoicedata['number'],
                    # "number":"100amar",
                    "date":odate,
                    "dueDate":pdate,
                    "contactCode":invoicedata['contactCode'],
                    # "contactCode":"CON-002",
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
                    "status": "INAP",
                    "gstnType": gstntype,
                }
            ]
            }
            Res2 = "Yes"
            print(Res2)
            print("End for loop")
            print(add_item)
            if (r.json()['status'] == 200):
                statusmsg = "SUCCESS"
                suc += 1
            else:
                statusmsg = "FAILED"
                fail += 1
            status = statusmsg
            remark = Res2
            module_type = "Sales Invoice"
            invoice_no = invoicedata['number']
            amount = invoicedata['totalamount']
            date = odate
            customer = invoicedata['contactCode']
            request_type_name = "POST"
            response_type_name = "SUCCESS"
            record_category_name = "SALES INVOICE SYNC"
            date_time_data = datetime.today().isoformat()
            tot = suc+fail
            modulesync = "Sales Invoice"
            cdate = now.strftime("%d"+"/"+"%m"+"/"+"%y" +
                                 " "+"%H"+":"+"%M"+":"+"%S")
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
                print("Batch Data Added successfully")
            else:
                print("SYNC SALES ORDER FAILED !!!!!!!")
        print("Projecr Done ---------------------------------------------------")
except:
    print("  I am in Except ------------==============--------------------")
