import requests
import json

url = "https://fmcrestapisandbox.cisco.com"
login_url = "/api/fmc_platform/v1/auth/generatetoken"
headers = {
    'Content-Type': 'applicaiton/json'
}
username = "username"
password = "password"

login_response = requests.post(f'{url}{login_url}', auth=(username, password), 
                                headers=headers, verify=False)

# FMC returns the token in response headers
# You must retrieve the token from the response object headers:
response_headers = login_response.headers
token = response_headers.get('X-auth-access-token', default=None)

#You would then use that token in the headers of following requests
print(token)