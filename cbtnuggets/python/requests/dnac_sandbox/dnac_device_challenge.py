import requests
import json
from dnac_auth import get_auth_token

# Challenge: Use the DNAC API to get a list devices and print out the device ID and IP address of each.

base_url = "https://sandboxdnac.cisco.com"
token = get_auth_token()

# Print number of devices to know how many repsonse to expect
count_url = base_url + "/dna/intent/api/v1/network-device/count"
headers = {
    "X-Auth-Token": token,
    "Accept": "application/json"
}
count = requests.get(count_url, headers=headers, verify=False).json()['response']

# Get a list of network devices
device_url = base_url + "/dna/intent/api/v1/network-device"
headers = {
    "X-Auth-Token": token,
    "Accept": "application/json"
}
devices = requests.get(device_url, headers=headers, verify=False).json()['response']
# print(json.dumps(devices, indent=4, sort_keys=True))
print(f"There are {count} devices:")
for device in devices:
    print(f"ID: {device['id']}")
    print(f"Management IP: {device['managementIpAddress']}")
    print()