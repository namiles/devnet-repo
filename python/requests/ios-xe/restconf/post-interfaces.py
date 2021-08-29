import requests
import json

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

for interface in range(700,751):
    print("Creating Loopback", interface, sep="")
    payload = json.dumps(
        {
            "ietf-interfaces:interface": {
                "name": f"Loopback{interface}",
                "description": "Added using RESTCONF abd Python - devnet",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": f"{interface}.1.1.1",
                            "netmask": "255.255.255.255"
                        }
                    ]
                }
            }
        }
    )
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)


