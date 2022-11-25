import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *
import json


API_KEY ='8bb4a94c72ffedf66794f6588cbb9283'
# PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
token='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'
API_VERSION='2022-07'



# url = "https://%s:%s@zia-warehouse.myshopify.com/admin/api/2022-07/customers.json" % (API_KEY, token)


url1='https://piyush1108.myshopify.com/admin/api/2022-07/customers.json'

# url4 = "https://piyush1108.myshopify.com/admin/api/2022-07/"


headers = {
			'Content-Type': 'application/json',
		   'X-Shopify-Access-Token':  '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'
		}

r = requests.get(url1, headers=headers)

data=r.json()

# print(data)





company=data['customers']

print(company)

# all_data={}

# for x in company:
# 	id1=x['id']
# 	email=x['email']
# 	fn=x['first_name']
# 	ln=x['last_name']
# 	ph=x['phone']
# 	note=x['note']
# 	if note == None:
# 		note="null"
# 	else:
# 		note=note[-15:]
# 	address1=x['addresses'][0]['address1']
# 	address2=x['addresses'][0]['address2']
# 	city=x['addresses'][0]['city']
# 	province1=x['addresses'][0]['province']
# 	pzip=x['addresses'][0]['zip']
# 	cont=x['addresses'][0]['country_name']
# 	all_data={'id':id1,'email':email,'fn':fn,'ln':ln,'ph':ph,'note':note,'address1':address1,'address2':address2,'city':city,'province':province1,'zip':pzip,'cont':cont}

# 	print(all_data)


# -------------------------------------------------------------Accounting Login-------------------------------------------

# url1 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/login"
# add_item = {
#         "username": "trilok.sharma@hostbooks.com",
#         "password":  "hbtax1234"
#       }
# headers = []
# r = requests.post(url1, json=add_item,  headers=headers)

# token=r.json()

# # print("value of token :-",token)

# value=token['data']['user']['accessToken']

# print("value of x-auth-token :-",value)

# value_preserve_key = token['data']['user']['preserveKey']


# print("value_preserve_key :- ",value_preserve_key)


# # GET COMPANY LIST CODE BY MR. ZIA --GET REQUEST

# url2="https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/companies"

# headers = {'x-auth-token': value, "x-version": "IND"}

# # print(headers)
# r = requests.get(url2, headers=headers)

# token2 = r.json()

# # comuid=token2['data']['comapanies'][0]['companyUID']
# # print("\n\ncompanyUID :- ",comuid)

# url3 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/validateUserLogin"

# headers = {
#         "x-version": "IND",
#         "x-preserveKey":  value_preserve_key,
#         "x-company":  "88E28C59-CE78-5B9B-44CA-38030F9746B0",
#         "x-forwarded-portal":  "true",
#         "Content-Type": "application/json"
#       }

# # print(headers)
# r = requests.get(url3, headers=headers)
# # print("Accounting Json :- ",r.json())

# uid=r.json()

# # print("companyUID :-",uid)



# # compuuid=uid['data']['user']['companyUUID']
# # print("companyUUID :- ",compuuid)



# # post data 
# # https://xxx.hostbooks.in/hostbook/api/master/add

# url4="https://sandboxin2accounts.hostbooks.in/hostbook/api/master/add"

# print("x-auth-token :-",value)
# print('x-preserveKey :-',value_preserve_key)


# url_header={
#         "Content-Type": "application/json",
# 		"x-auth-token": value,
# 		"x-preserveKey":  value_preserve_key,
#         "x-company": "88E28C59-CE78-5B9B-44CA-38030F9746B0"
# }

# print(url_header)

# add_item = '''{"contactList": [{"name": "SiteCustomer", "accountNumber": 5202798051457, "employee": false, "vendor": false, "customer": true, "primaryType": "customer", "contactPerson": [{"emailAddress": "test3@gmail.com", "firstName": "Site", "lastName": "Customer", "primeFlag": 1}], "pan": "AATFV1949G", "creditLimit": null, "email": null, "phone": null, "mobile": null, "skype": null, "website": null, "address": [{"addressGSTIN": "36AATFV1949G1ZL", "note": null, "address1": "address billing", "address2": "house no 20", "street": null, "city": "Gurugram", "state": "Haryana", "zip": "124016", "country": "India", "mobile": null, "pan": null, "tan": null, "gstin": null, "cin": null, "telephone": null, "type": "PADR"}], "contactGstin": [{"number": "36AATFV1949G1ZL", "note": null, "verified": false, "billingAddress": {"addressGSTIN": "36AATFV1949G1ZL", "note": null, "address1": "address billing", "address2": "house no 20", "street": null, "city": "Gurugram", "state": "Haryana", "zip": "124016", "country": "India", "mobile": null, "pan": null, "tan": null, "gstin": null, "cin": null, "telephone": null, "type": "BADR"}, "shippingAddress": {"addressGSTIN": "36AATFV1949G1ZL", "note": null, "address1": "address billing", "address2": "house no 20", "street": null, "city": "Gurugram", "state": "Haryana", "zip": "124016", "country": "India", "mobile": null, "pan": null, "tan": null, "gstin": null, "cin": null, "telephone": null, "type": "SADR"}, "defaultGstin": true}], "openingBalance": 0, "openingDate": null, "notes": null, "termsAndCondition": null, "status": "COAC", "cinNumber": null, "panVerified": false, "fax": null}]}'''




# dict1 = json.loads(add_item)
# dict2 = json.stringify(add_item)
# print(dict2)


# dict1 = json.loads(add_item)
# print(dict1)
# print("Rahul")

# r = requests.post(url4, json=dict1,  headers=url_header)

# print(r.text)


#  Mydata 

# {'contactList': [{'name': 'SiteCustomer', 'accountNumber': 5202798051457, 'employee': False, 'vendor': False, 'customer': True, 'primaryType': 'customer', 'contactPerson': [{'emailAddress': 'test3@gmail.com', 'firstName': 'Site', 'lastName': 'Customer', 'primeFlag': 1}], 'pan': 'AATFV1949G', 'creditLimit': None, 'email': None, 'phone': None, 'mobile': None, 'skype': None, 'website': None, 'address': [{'addressGSTIN': '36AATFV1949G1ZL', 'note': None, 'address1': 'address billing', 'address2': 'house no 20', 'street': None, 'city': 'Gurugram', 'state': 'Haryana', 'zip': '124016', 'country': 'India', 'mobile': None, 'pan': None, 'tan': None, 'gstin': None, 'cin': None, 'telephone': None, 'type': 'PADR'}], 'contactGstin': [{'number': '36AATFV1949G1ZL', 'note': None, 'verified': False, 'billingAddress': {'addressGSTIN': '36AATFV1949G1ZL', 'note': None, 'address1': 'address billing', 'address2': 'house no 20', 'street': None, 'city': 'Gurugram', 'state': 'Haryana', 'zip': '124016', 'country': 'India', 'mobile': None, 'pan': None, 'tan': None, 'gstin': None, 'cin': None, 'telephone': None, 'type': 'BADR'}, 'shippingAddress': {'addressGSTIN': '36AATFV1949G1ZL', 'note': None, 'address1': 'address billing', 'address2': 'house no 20', 'street': None, 'city': 'Gurugram', 'state': 'Haryana', 'zip': '124016', 'country': 'India', 'mobile': None, 'pan': None, 'tan': None, 'gstin': None, 'cin': None, 'telephone': None, 'type': 'SADR'}, 'defaultGstin': True}], 'openingBalance': 0, 'openingDate': None, 'notes': None, 'termsAndCondition': None, 'status': 'COAC', 'cinNumber': None, 'panVerified': False, 'fax': None}]}


#accounting 

# {'contactList': [{'name': 'SiteCustomer', 'accountNumber': 5202798051457, 'employee': False, 'vendor': False, 'customer': True, 'primaryType': 'customer', 'contactPerson': [{'emailAddress': 'test3@gmail.com', 'firstName': 'Site', 'lastName': 'Customer', 'primeFlag': 1}], 'pan': 'AATFV1949G', 'creditLimit': None, 'email': None, 'phone': None, 'mobile': None, 'skype': None, 'website': None, 'address': [{'addressGSTIN': '36AATFV1949G1ZL', 'note': None, 'address1': 'address billing', 'address2': 'house no 20', 'street': None, 'city': 'Gurugram', 'state': 'Haryana', 'zip': '124016', 'country': 'India', 'mobile''''{"contactList": [{"name": "SiteCustomer", "accountNumber": 5202798051457, "employee": false, "vendor": false, "customer": true, "primaryType": "customer", "contactPerson": [{"emailAddress": "test3@gmail.com", "firstName": "Site", "lastName": "Customer", "primeFlag": 1}], "pan": "AATFV1949G", "creditLimit": null, "email": null, "phone": null, "mobile": null, "skype": null, "website": null, "address": [{"addressGSTIN": "36AATFV1949G1ZL", "note": null, "address1": "address billing", "address2": "house no 20", "street": null, "city": "Gurugram", "state": "Haryana", "zip": "124016", "country": "India", "mobile": null, "pan": null, "tan": null, "gstin": null, "cin": null, "telephone": null, "type": "PADR"}], "contactGstin": [{"number": "36AATFV1949G1ZL", "note": null, "verified": false, "billingAddress": {"addressGSTIN": "36AATFV1949G1ZL", "note": null, "address1": "address billing", "address2": "house no 20", "street": null, "city": "Gurugram", "state": "Haryana", "zip": "124016", "country": "India", "mobile": null, "pan": null, "tan": null, "gstin": null, "cin": null, "telephone": null, "type": "BADR"}, "shippingAddress": {"addressGSTIN": "36AATFV1949G1ZL", "note": null, "address1": "address billing", "address2": "house no 20", "street": null, "city": "Gurugram", "state": "Haryana", "zip": "124016", "country": "India", "mobile": null, "pan": null, "tan": null, "gstin": null, "cin": null, "telephone": null, "type": "SADR"}, "defaultGstin": true}], "openingBalance": 0, "openingDate": null, "notes": null, "termsAndCondition": null, "status": "COAC", "cinNumber": null, "panVerified": false, "fax": null}]}'''


