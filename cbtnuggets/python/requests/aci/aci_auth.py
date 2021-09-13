import requests
import json

def aci_auth():
    """
    Logs into ACI always-on sandbox and returns token.
    """
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
     
    return token