import requests
import json

# Dont forget sudo ufw allow 8080
url_base = 'https://sandbox-nso-1.cisco.com'
auth = ("developer", "Services4Ever")

# Other useful headers

#    'application/vnd.yang.api+json',
#    'application/vnd.yang.datastore+json',
#    'application/vnd.yang.data+json',


headers = {'Accept': 'application/vnd.yang.collection+json'}

# Get request to NSO
response = requests.get(f'{url_base}/data/tailf-ncs:devices/device', auth=auth, headers=headers)
print(response)
# print(json.dumps(response, indent=2, sort_keys=True))

# # Parse out devices from response body
# devices = response['collection']['tailf-ncs:device']
# for device in devices:
#     print(f"Name: {device['name']}")
#     print(f"IP: {device['address']}")
#     print(f"SSH Port: {device['port']}")
#     print(f"Auth Group: {device['authgroup']}")
#     # print(device)
#     print(" ")