import requests
import json
from routers import router1

#Allow self signed certificates
requests.packages.urllib3.disable_warnings()

url = f"https://{router1['HOST']}:{router1['PORT']}/restconf/data/ietf-interfaces:interfaces-state"

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
}

#Run GET
response = requests.get(url, auth=(router1['USER'], router1['PASS']), headers=headers, verify=False)

print('\n', '*' * 100, '\n', sep="")

print(response.json())
print(type(response.json()))

print('\n', '*' * 100, '\n', sep="")

interface_data = response.json()
print(type(interface_data))

print('\n', '*' * 100, '\n', sep="")

interface_data_formatted = json.dumps(response.json(), indent=2)
print(interface_data_formatted)
print(type(interface_data_formatted))

print('\n', '*' * 100, '\n', sep="")


