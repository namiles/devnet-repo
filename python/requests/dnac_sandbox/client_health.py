import requests
import json

# Get token with DNAC 2
user = "devnetuser"
passw = "Cisco123!"
dnac_url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
tokenResponse = requests.post(dnac_url, auth=(user, passw)).json()
token = tokenResponse["Token"]

# Client health using DNAC

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

headers = {
    "X-Auth-Token":token
}

response = requests.get(url, headers=headers)
jsonData = response.json()
prettyJsonData = json.dumps(jsonData, indent=2)

print(prettyJsonData)