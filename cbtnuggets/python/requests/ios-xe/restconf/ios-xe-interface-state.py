import requests
import json
from routers import router1

#Allow self signed certificates
requests.packages.urllib3.disable_warnings()

# http://<ip addres>:<port>/<root>/<data store>/<[yang-module]:container>/<leaf>?=options
url = f"https://{router1['HOST']}:{router1['PORT']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=Loopback1799"
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
}

response = requests.get(url, headers=headers, verify=False, auth=(router1['USER'], router1['PASS']))

if response.ok:
  response_json = response.json()
  print(type(response_json))

  print('\n', '*' * 100, '\n', sep="")

  print(json.dumps(response_json, indent=4))

  print('\n', '*' * 100, '\n', sep="")

  print(f"Interface: {response_json['Cisco-IOS-XE-interfaces-oper:interface']['name']}")
  print(f"Description: {response_json['Cisco-IOS-XE-interfaces-oper:interface']['description']}")
  print(f"IPv4 Address: {response_json['Cisco-IOS-XE-interfaces-oper:interface']['ipv4']}")
  if response_json['Cisco-IOS-XE-interfaces-oper:interface']['admin-status'] == 'if-state-up':
      print("Admin State: Up")
  else:
      print("Admin State: Down")

  print('\n', '*' * 100, '\n', sep="")
else:
  print(f"Error occurred with status code {response.status_code}")
