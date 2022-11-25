import shopify
import requests
from shopify.base import ShopifyResource
from shopify.resources import *
import json

# Shopify login authentication
API_KEY = '8bb4a94c72ffedf66794f6588cbb9283'
# PASSWORD ='c552f37f1f65be68f64a87f0cf73634d'
token = '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'
API_VERSION = '2022-07'


# Accounting Authentication
def login():
    global value
    global value_preserve_key
    url1 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/login"
    add_item = {
        "username": "trilok.sharma@hostbooks.com",
        "password":  "hbtax1234"
    }

    headers = []
    r = requests.post(url1, json=add_item,  headers=headers)
    token = r.json()
    value = token['data']['user']['accessToken']
    value_preserve_key = token['data']['user']['preserveKey']

    url2 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/companies"
    headers = {
        'x-auth-token': value,
        "x-version": "IND"
    }

    r = requests.get(url2, headers=headers)
    token2 = r.json()

    url3 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/validateUserLogin"
    headers = {
        "x-version": "IND",
        "x-preserveKey":  value_preserve_key,
        "x-company":  "88E28C59-CE78-5B9B-44CA-38030F9746B0",
        "x-forwarded-portal":  "true",
        "Content-Type": "application/json"
    }
    r = requests.get(url3, headers=headers)
    # print(r.json())


# <------------------------------------------------------------------------------------------------------------------------->

# Customer details

def customer_details():
    global all_data
    url1 = 'https://piyush1108.myshopify.com/admin/api/2022-07/customers.json'
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token':  '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'
    }
    r = requests.get(url1, headers=headers)
    data = r.json()
    print("customers json data :-", data)

    company = data['customers']
    for x in company:
        id1 = x['id']
        email = x['email']
        fn = x['first_name']
        ln = x['last_name']
        ph = x['phone']
        note = x['note']
        address1 = x['addresses'][0]['address1']
        address2 = x['addresses'][0]['address2']
        city = x['addresses'][0]['city']
        province = x['addresses'][0]['province']
        pzip = x['addresses'][0]['zip']
        cont = x['addresses'][0]['country_name']
        all_data = {'id': id1, 'email': email, 'fn': fn, 'ln': ln, 'ph': ph, 'note': note, 'address1': address1,
                    'address2': address2, 'city': city, 'province': province, 'zip': pzip, 'cont': cont}

        return all_data
    

# Post all customer_details data in Accounting
def customerdata_post(all_data, value, value_preserve_key):
    url4 = "https://sandboxin2accounts.hostbooks.in/hostbook/api/master/add"
    url_header = {
        "Content-Type": "application/json",
        "x-auth-token": value,
        "x-preserveKey":  value_preserve_key,
        "x-company": "88E28C59-CE78-5B9B-44CA-38030F9746B0"
    }

    print("Url header :- ", url_header)



    add_item = {'contactList': [{'name': all_data['fn'] + all_data['ln'], 'accountNumber': all_data['id'], 'employee': False, 'vendor': False, 'customer': True, 'primaryType': 'customer', 'contactPerson': [{'emailAddress':all_data['email'], 'firstName': all_data['fn'], 'lastName': all_data['ln'], 'primeFlag': 1}], 'pan': 'AATFV1949G', 'creditLimit': None, 'email': None, 'phone': None, 'mobile': all_data['ph'], 'skype': None, 'website': None, 'address': [{'addressGSTIN': '36AATFV1949G1ZL', 'note': None, 'address1': 'address billing', 'address2': 'house no 20', 'street': None, 'city': 'Gurugram', 'state': 'Haryana', 'zip': '124016', 'country': 'India', 'mobile': None, 'pan': None, 'tan': None, 'gstin': None, 'cin': None, 'telephone': None, 'type': 'PADR'}], 'contactGstin': [{'number': '36AATFV1949G1ZL', 'note': None, 'verified': False, 'billingAddress': {'addressGSTIN': '36AATFV1949G1ZL', 'note':all_data['note'], 'address1': all_data['address1'], 'address2': all_data['address2'], 'street': None, 'city': all_data['city'], 'state': all_data['province'], 'zip': all_data['zip'], 'country':  all_data['cont'], 'mobile': None, 'pan': None, 'tan': None, 'gstin': None, 'cin': None, 'telephone': None, 'type': 'BADR'}, 'shippingAddress': {'addressGSTIN': '36AATFV1949G1ZL', 'note':all_data['note'], 'address1': all_data['address1'], 'address2': all_data['address2'], 'street': None, 'city': all_data['city'], 'state': all_data['province'], 'zip': all_data['zip'], 'country':  all_data['cont'], 'mobile': None, 'pan': None, 'tan': None, 'gstin': None, 'cin': None, 'telephone': None, 'type': 'SADR'}, 'defaultGstin': True}], 'openingBalance': 0, 'openingDate': None, 'notes': None, 'termsAndCondition': None, 'status': 'COAC', 'cinNumber': None, 'panVerified': False, 'fax': None}]}


    print("Rahul")

    r = requests.post(url4, json=add_item,  headers=url_header)

    print(r.json())


login()
data=customer_details()

print("Hello-------------",data)

customerdata_post(data, value, value_preserve_key)
