import requests
import json

from requests.api import head

#read-only sandbox key
X_CISCO_MERAKI_API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

headers = {
    "X-Cisco-Meraki-API-Key": X_CISCO_MERAKI_API_KEY
}

base_url = "https://api.meraki.com/api/v1"

#organizations
org_url = base_url+"/organizations"
org_response = requests.get(org_url, headers=headers, verify=False).json()
for org in org_response:
    print(org['name'])
    print("ID:", org['id'])
    print()
