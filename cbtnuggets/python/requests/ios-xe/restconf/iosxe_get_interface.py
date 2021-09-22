import requests
from routers import router1

url = f"https://{router1['HOST']}:{router1['PORT']}/restconf/data/ietf-interfaces:interfaces"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
