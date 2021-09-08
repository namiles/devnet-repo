import requests
import json
from dnac_auth import get_auth_token

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"

headers = {
    "X-Auth-Token": get_auth_token()
}

response = requests.get(url, headers=headers)
jsonData = response.json()
prettyJsonData = json.dumps(jsonData, indent=2)

print(prettyJsonData)