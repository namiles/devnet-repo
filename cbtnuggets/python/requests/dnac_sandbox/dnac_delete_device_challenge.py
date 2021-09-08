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
device_url = base_url + "/dna/intent/api/v1/network-device/f16955ae-c349-47e9-8e8f-9b62104ab604"

response = requests.post(device_url, headers=headers, verify=False).json()
print(response)

