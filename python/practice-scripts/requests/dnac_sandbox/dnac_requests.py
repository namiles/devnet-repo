import requests
from requests.models import HTTPBasicAuth

# Function to get access token from DNAC sandbox
def get_token():
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    user = 'devnetuser'
    password = 'Cisco123!'
    headers = {'content-type': 'application/json'},
    token = requests.post(url, auth=HTTPBasicAuth(username=user, password=password), headers=headers, verify=False,)
    data = token.json()
    print(data)
    return data['Token']

token = get_token
print(token)