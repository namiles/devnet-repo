import requests
import json
from dnac_auth import get_auth_token

# Challenge: Use the DNAC API to create a new device and list the devices to see the new device.

base_url = "https://sandboxdnac.cisco.com"
token = get_auth_token()
headers = {
    "X-Auth-Token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Create a new device
device_url = base_url + "/dna/intent/api/v1/network-device"
payload = {
    "type":"New device posted"
}
create_device_response = requests.post(device_url, data=json.dumps(payload),headers=headers, verify=False).json()
print(create_device_response)

# # Get a list of network devices
# devices = requests.get(device_url, headers=headers, verify=False).json()['response']
# # print(json.dumps(devices, indent=4, sort_keys=True))
# for device in devices:
#     print(f"ID: {device['id']}")
#     print(f"Management IP: {device['managementIpAddress']}")
#     print()