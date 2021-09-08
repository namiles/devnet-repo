import requests
import json

def get_auth_token():
    """ Returns an API token from the always-on cisco devnet sandbox"""
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    user = 'devnetuser'
    pw = 'Cisco123!'
    response = requests.post(url, auth=(user, pw)).json()
    token = response['Token']
    return token