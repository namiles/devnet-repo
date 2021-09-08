import requests
import json
from dnac_auth import get_auth_token

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

headers = {
    "X-Auth-Token": get_auth_token()
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

