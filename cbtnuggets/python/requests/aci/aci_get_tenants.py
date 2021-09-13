import requests
import json
from aci_auth import aci_auth

cookies = {}
cookies["APIC-Cookie"] = aci_auth()

# Get Tenants
tenants_url = "https://sandboxapicdc.cisco.com:443/api/class/fvTenant.json"

tn_response = requests.get(tenants_url, cookies=cookies).json()
print(json.dumps(tn_response, indent=4))