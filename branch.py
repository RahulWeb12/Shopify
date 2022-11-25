import shopify
import requests

url1 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/login"
add_item = {
    "username": "piyushqa2018a@gmail.com",
    "password":  "test@123"
}

r = requests.post(url1, json=add_item)
token = r.json()
# print("Token1 :-",token)
value = token['data']['user']['accessToken']
print(value)
value_preserve_key = token['data']['user']['preserveKey']
print(value_preserve_key)
url2 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/companies"
headers = {
    'x-auth-token': value,
    "x-version": "IND"
}

r1 = requests.get(url2, headers=headers)

token2 = r1.json()
# print("Token 2 :-",token2)

companyUID = token2["data"]["comapanies"][0]["companyUID"]
url3 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/validateUserLogin"
headers = {
    "x-version": "IND",
    "x-preserveKey":  value_preserve_key,
    # "x-company":  "F941FF61-7FAA-DD71-919B-1AE3F013013E",
    # "x-company":  "389B7CCF-2F78-AC7B-ECD8-87FDEDE3E083",
    "x-company":  companyUID,
    "x-forwarded-portal":  "true",
    "Content-Type": "application/json"
}

r2 = requests.get(url3, headers=headers)
token3 = r2.json()
# print("Token 3 :-",token3)

branchurl="https://sandboxin2accounts.hostbooks.in/hostbook/api/master/list"

headers1={
    "Content-Type": "application/json",
    "x-preserveKey":  value_preserve_key,
    "x-company":  companyUID,
    'x-auth-token': value,
}

add_item={
    "page":1,
    "limit":20,
    "entityType":"BRANCH"
}

r3 = requests.post(branchurl, headers=headers1,json=add_item)
token4 = r3.json()


print("Token 4:-",token4)


