import requests

url = "https://sandbox-nso-1.cisco.com:443/restconf/data/tailf-ncs:devices/device-group"
username = "developer"
password = "Services4Ever"

# Other headers
# 'application/vnd.yang.api+json',
# 'application/vnd.yang.datastore+json', 
# 'application/vnd.yang.data+json'

payload = ""
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
}

response = requests.get(url, auth=(username, password), headers=headers, data=payload)

print(response.text)
