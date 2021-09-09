import requests
import json

#Allow self signed certificates
requests.packages.urllib3.disable_warnings()

#Credentials
user = 'developer'
password = 'C1sco12345'

#URL to use for API Call
url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces'

#Set yang+jason as the data formats
headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

#Run GET
response = requests.get(url, auth=(user, password), headers=headers, verify=False)

print(response.json())
print(type(response.json()))
print()

interface_data = response.json()
print(type(interface_data))
print()

interface_data_formatted = json.dumps(response.json(), indent=2)
print()
print(interface_data_formatted)
print(type(interface_data_formatted))
print()


