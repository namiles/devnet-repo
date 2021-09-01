import requests
import json

################ LOGIN ######################
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
user = 'devnetuser'
pw = 'Cisco123!'
response = requests.post(url, auth=(user, pw)).json()
token = response['Token']

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

headers = {
    "X-Auth-Token": token
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    jsonData = response.json()
    prettyJsonData = json.dumps(jsonData, indent=2)
    print(prettyJsonData)
else:
    # Oops something went wrong...  Better do something about it.
    print("\nError ocurred. See below.")
    print(response.status_code, response.text)

