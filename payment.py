from locale import currency
from operator import inv
import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *
import json


# ---------------------- Get payment data -----------------------------------------

url6 = "https://gcl-ecommerce.myshopify.com/admin/api/2022-07/orders.json?status=any"

headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": "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"
}

r = requests.get(url6, headers=headers)

data1 = r.json()
data2 = data1['orders']
ordid = []
suc1 = 0
fail1 = 0

for val in data2:
    id3 = val['id']
    ordid.append(id3)
    order_number = val['order_number']
    accountCode = val['customer']['id']
    buyerOrderDate1 = val['created_at']
    y = buyerOrderDate1.split('T')[0].split('-')
    buyerOrderDate = y[2]+"-"+y[1]+"-"+y[0]
 # ---------------------- Accounting Login -----------------------------------------

url1 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/login"
add_item = {
            "username": "ashish.baranwal@hostbooks.com",
            "password":  "12345678"
        }
r = requests.post(url1, json=add_item)
token = r.json()
        # print(token)
value = token['data']['user']['accessToken']
value_preserve_key = token['data']['user']['preserveKey']
url2 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/companies"
headers = {
    'x-auth-token': value,
    "x-version": "IND"
}
print("I am waiting..........")
r = requests.get(url2, headers=headers)
token2 = r.json()
companyUID = token2["data"]["comapanies"][0]["companyUID"]
print("companyUID :- ", companyUID)
print(" The wait is over.....")
url3 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/validateUserLogin"
headers = {
                    "x-version": "IND",
                    "x-preserveKey":  value_preserve_key,
                    "x-company":  "F941FF61-7FAA-DD71-919B-1AE3F013013E",
                    # "x-company":  companyUID,
                    "x-forwarded-portal":  "true",
                    "Content-Type": "application/json"
                }
r = requests.get(url3, headers=headers)
print(
            "*********************  Validate user Url  ******************************")
token3 = r.json()
for idd in ordid:
    # ---------------------- Get payment data -----------------------------------------
    url5 = "https://gcl-ecommerce.myshopify.com/admin/api/2022-10/orders/%s/transactions.json" % (
        idd)
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": "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"
    }
    r = requests.get(url5, headers=headers)
    trans = r.json()

    if(trans['transactions'][0]['status'] == "success"):
        suc1 += 1
        currencyCode = trans['transactions'][0]['receipt']['x_currency']
        at1 = trans['transactions'][0]['processed_at'].split('T')[0].split('-')
        processed_at = at1[2]+"-"+at1[1]+"-"+at1[0]
        numberid = trans['transactions'][0]['id']
        amount = trans['transactions'][0]['amount']
        reference = trans['transactions'][0]['receipt']['x_reference']
        other_reference = trans['transactions'][0]['receipt']['x_gateway_reference']
        unit_price = trans['transactions'][0]['receipt']['x_amount']

       

        # ---------------------------------- Post Data On Accounting------------------------------------

        url4 = "https://sandboxin2accounts.hostbooks.in/hostbook/api/transaction/add"
        url_header = {
            "Content-Type": "application/json",
            "x-auth-token": value,
            "x-preserveKey":  value_preserve_key,
            "x-company": "F941FF61-7FAA-DD71-919B-1AE3F013013E"
        }

        postdata = {
            "receiveMoneyList":
                    [
                        {
                            "taxType": "NTAX",
                            "currencyCode":currencyCode,
                            "exchangeRate": 1,
                            "companyGstin": "37AABCB5803G1ZY",
                            "branch": "H.O",
                            "category": "",
                            "bankCode": "HD0001",
                            "bankName": "HDFC Bank",
                            "txnType": "ROA",
                            "date": processed_at,
                            "number": numberid,
                            "amount": amount,
                            "buyerOrderNumber": order_number,
                            "buyerOrderDate": buyerOrderDate,
                            "reference": reference,
                            "otherReference": other_reference,
                            "termsOfPayment": None,
                            "lineItems": [
                                {
                                    "quantity": 1,
                                    "unitPrice": unit_price,
                                    "amount": unit_price,
                                    "accountCode": accountCode,
                                    "accountName": "",
                                    "description": "Shopify Payment",
                                }
                            ],
                            "typeCode": "SSMP",
                        }
                    ]
                    }
        r = requests.post(url4, json=postdata,  headers=url_header)
        print(r.json())
        print("My post data ------------------------",postdata)
        print("Successfull posted ........ ", idd)

    else:
        fail1 += 1
        print("Status is Pending  !!!!!!!! ", idd)

print("Total Success is :- ", suc1)
print("Total Failed is :- ", fail1)







# ---------------------- Get data from salesorder -----------------------------------------


# url = "https://piyush1108.myshopify.com/admin/api/2022-07/orders.json?status=any"
# headers = {"Content-Type": "application/json",
#            "X-Shopify-Access-Token": "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"}

# r = requests.get(url, headers=headers)
# sales = r.json()
# data = sales["orders"]
# buyerOrderDate = []
# buyerOrderNumber = []
# accountCode = []
# for val in data:
#     cdate = val['created_at']
#     y = cdate.split('T')[0].split('-')
#     oidate = y[2]+"-"+y[1]+"-"+y[0]
#     buyerOrderDate.append(oidate)
#     odnum = val['order_number']
#     buyerOrderNumber.append(odnum)
#     accCode = val['id']  # customer ---->id
#     accountCode.append(accCode)
# print('buyerOrderDate',buyerOrderDate)
# print('buyerOrderNumber',buyerOrderNumber)
# print('accountCode',accountCode)