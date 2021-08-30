import requests
import json

def get_token():
    """
    Returns token for interacting with NX-API REST in string format.
    """

    #Reservable NS-OX single node sandbox - developer.cisco.com
    url = "https://10.10.20.58/api/aaaLogin.json"
    payload = json.dumps({
        "aaaUser": {
            "attributes": {
                "name": "admin",
                "pwd": "Cisco123"
            }
        }
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=payload, verify=False).json()
    token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]

    return token
