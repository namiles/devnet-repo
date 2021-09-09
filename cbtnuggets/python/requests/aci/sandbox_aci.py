import requests
import json

username = "admin"
password = "ciscopsdt"

#Allow self signed certificates
requests.packages.urllib3.disable_warnings()

# Login and get access token
auth_url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "!v3G@!4@Y"
    }
  }
})

headers = {
    "Content-Type": "application/json"
}

#Get reponse and convert to python dict using .json()
auth_response = requests.post(auth_url, data=payload, headers=headers).json()

#Parse token and create cookie
token = auth_response["imdata"][0]["aaaLogin"]["attributes"]["token"]
print(token)
cookies = {}
cookies["APIC-Cookie"] = token

print("\n######################################################################################################################\n")

# Get Tenants
tenants_url = "https://sandboxapicdc.cisco.com:443/api/class/fvTenant.json"

tn_response = requests.get(tenants_url, cookies=cookies).json()
print(json.dumps(tn_response, indent=4))

print("\n######################################################################################################################\n")

# Get application profile and set description then get it again
ap_url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

ap_response = requests.get(ap_url, cookies=cookies).json()
print("\nBefore desc change")
print(json.dumps(ap_response, indent=4))

payload = {
    "fvAp": {
        "attributes": {
            "descr": "Changed with REST API",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
    }
}

#Post the change
print("\nPosting desc change")
ap_response2 = requests.post(ap_url, cookies=cookies, data=json.dumps(payload)).json()

ap_response2 = requests.get(ap_url, cookies=cookies).json()
print("\nAfter desc change")
print(json.dumps(ap_response2, indent=4))

print("\n######################################################################################################################\n")

