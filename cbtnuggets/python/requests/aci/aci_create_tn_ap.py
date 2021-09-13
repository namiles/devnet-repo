import requests
import json
from aci_auth import aci_auth

cookies = {}
cookies["APIC-Cookie"] = aci_auth()

# Tenants
tenants_url = "https://sandboxapicdc.cisco.com:443/api/class/fvTenant.json"

payload = {
    "fvTenant": {
        "attributes": {
            "name": "nick_python_tenant"
        }
    }
}

tn_response = requests.post(tenants_url, data=json.dumps(payload), cookies=cookies).json()
print(json.dumps(tn_response, indent=4))
