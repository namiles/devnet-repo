import requests
import json
from routers import router1

#Allow self signed certificates
requests.packages.urllib3.disable_warnings()

url = f"https://{router1['HOST']}:{router1['PORT']}/restconf/data/ietf-interfaces:interfaces"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback1799",
    "description": "hey cla",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "1.7.9.9",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.post(url, headers=headers, data=payload, verify=False)
print(response.status_code)
print(response.text)
