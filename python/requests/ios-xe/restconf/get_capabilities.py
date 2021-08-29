import requests
import json
from routers import router1

#Allow self signed certificates
requests.packages.urllib3.disable_warnings()

# http://<ip addres>:<port>/<root>/<data store>/<[yang-module]:container>/<leaf>?=options
url = f"https://{router1['HOST']}:{router1['PORT']}/restconf/data/netconf-state/capabilities"
root_url = f"https://{router1['HOST']}:{router1['PORT']}/.well-known/host-meta"

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
}

response = requests.get(url, headers=headers, verify=False, auth=(router1['USER'], router1['PASS']))

if response.ok:
  print(response)
  response_json = response.json()
  print(type(response_json))

  print('\n', '*' * 100, '\n', sep="")

  print(json.dumps(response_json, indent=4))

  print('\n', '*' * 100, '\n', sep="")
else:
  print(f"Error occurred with status code {response.status_code}")

root_response = requests.get(root_url, headers=headers, verify=False, auth=(router1['USER'], router1['PASS']))
print(root_response.status_code)
print(root_response.text)
