import requests
import json
from aci_auth import aci_auth

cookies = {}
cookies["APIC-Cookie"] = aci_auth()

# Get Aps
Ap_url = "https://sandboxapicdc.cisco.com:443/api/class/fvAp.json"

ap_response = requests.get(Ap_url, cookies=cookies).json()
print(json.dumps(ap_response, indent=4))