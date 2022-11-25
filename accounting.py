import requests
import json



# LOGIN API CODE BY MR. ZIA --POST REQUEST

url1 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/login"

add_item = {
        "username": "trilok.sharma@hostbooks.com",
        "password":  "hbtax1234"
      }
headers = []
# r = requests.post(url1, json=add_item,  headers=headers)
r = requests.post(url1, json=add_item,  headers=headers)

token=r.json()
# print(token)

value=token['data']['user']['accessToken']
value_preserve_key = token['data']['user']['preserveKey']
print(value)


# # GET COMPANY LIST CODE BY MR. ZIA --GET REQUEST

url2="https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/companies"

headers = {'x-auth-token': value, "x-version": "IND"}

# print(headers)
r = requests.get(url2, headers=headers)

token2 = r.json()
print("token2 :-",token2)


# comuid=token2['data']['comapanies'][0]['companyUID']
# print("\n\ncompanyUID :- ",comuid)

url3 = "https://sandboxinapiaccounts.hostbooks.in/securitycenter/user/validateUserLogin"

headers = {
        "x-version": "IND",
        "x-preserveKey":  value_preserve_key,
        "x-company":  "88E28C59-CE78-5B9B-44CA-38030F9746B0",
        "x-forwarded-portal":  "true",
        "Content-Type": "application/json"


      }

print(headers)
r = requests.get(url3, headers=headers)



print(r.json())

# cuuid=r.json()

# comuuid=cuuid['data']['user']['companyUUID']

# print("companyUUID :-",comuuid)

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''']




