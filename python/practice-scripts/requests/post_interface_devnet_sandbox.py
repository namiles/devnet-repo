import requests
import json

#Allow self signed certificates
requests.packages.urllib3.disable_warnings()

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

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

print(response.text)
