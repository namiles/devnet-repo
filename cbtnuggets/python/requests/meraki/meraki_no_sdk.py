import requests
import json

requests.packages.urllib3.disable_warnings()

#read-only sandbox key
X_CISCO_MERAKI_API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

headers = {
    "X-Cisco-Meraki-API-Key": X_CISCO_MERAKI_API_KEY
}

base_url = "https://api.meraki.com/api/v1"

#organizations
org_url = base_url+"/organizations"
org_response = requests.get(org_url, headers=headers, verify=False)

if org_response.ok:
    org_response = org_response.json()
    print()
    for org in org_response:
        if org['name'] == "DevNet Sandbox":
            devnet_org_id = org['id']
            print(org['name'])
            print("ID:", org['id'])
    print()
    if devnet_org_id:
        networks = requests.get(f"{base_url}/organizations/{devnet_org_id}/networks", headers=headers, verify=False)
        if networks.ok:
            networks = networks.json()
            for network in networks:
                if network["name"] == "DevNet Sandbox ALWAYS ON":
                    devnet_network_id = network['id']
                    print(devnet_network_id)
        else:
            print("Request for networks failed.")
            print(networks.status_code)
        print()
    if devnet_network_id:
        devices = requests.get(f"{base_url}/networks/{devnet_network_id}/devices", headers=headers, verify=False)
        if devices.ok:
            devices = devices.json()
            for device in devices:
                print(f"Model: {device['model']:<8}")
        else:
            print("Request for devices failed.")
            print(devices.status_code)
else:
    print("Request failed. See status code below.")
    print(org_response.status_code)