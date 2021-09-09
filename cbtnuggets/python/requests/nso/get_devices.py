import requests

url = "https://sandbox-nso-1.cisco.com:443/restconf/data/tailf-ncs:devices/device"
username = "developer"
password = "Services4Ever"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
}

response = requests.get(url, auth=(username, password), headers=headers, data=payload)

print(response.text)
