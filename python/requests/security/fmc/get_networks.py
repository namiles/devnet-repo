import requests
import json
import sys

base_url = "https://fmcrestapisandbox.cisco.com"
login_url = "/api/fmc_platform/v1/auth/generatetoken"
headers = {
    'Content-Type':'application/json'
}

#Credentials from Sandbox email
temp_user = 'NicholasMi'
temp_password = 'nE9FHTD6'

#Login and get token
login_response = requests.post(f'{base_url}{login_url}', auth=(temp_user,temp_password), verify=False)

if not login_response.ok:
    print("Login failed, check for errors in request or check if sandbox is up.")
    sys.exit(1)
else:
    print("Login successful. Getting token.")
    login_resp_headers = login_response.headers
    #Grab token from headers
    token = login_resp_headers.get('X-auth-access-token', default=None)
    #Add token to headers
    headers['X-auth-access-token'] = token
    networks_url = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks'
    networks_response = requests.get(f'{base_url}{networks_url}', headers=headers, verify=False).json()
    print(json.dumps(networks_response, indent=4))