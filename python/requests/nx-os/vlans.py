import requests
import json
from login import get_token

url = "https://10.10.20.58/api/node/class/l2BD.json"
token = get_token()
cookies = {}
cookies['APIC-cookie'] = token
headers = {
  'Content-Type': 'application/json',
  'Accept':'application/json'
}

response = requests.get(url, headers=headers, cookies=cookies, verify=False).json()

print("\n Token: ", token, "\n")
print(json.dumps(response, indent=2, sort_keys=True))
