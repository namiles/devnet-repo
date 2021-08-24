import requests
import sys
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = 'https://sandbox-sdwan-1.cisco.com/j_security_check'
login_body = {
    'j_username':'devnetuser',
    'j_password':'RG!_Yw919_83'
}

session = requests.session()
response = session.post(auth_url, data=login_body, verify=False) #post in the actual python dictionary, not a converted string with dumps

'''
Response always returns 200 OK unless an errored occurs
If the response body contains any text, then auth failed.
'''
if not response.ok or response.text:
    print('login failed')
    sys.exit(1)
else:
    print('log in successful\n')

# Get Templates
device_url = 'https://sandbox-sdwan-1.cisco.com/dataservice/server/info'
device_response = session.get(device_url, verify=False).json()
print(json.dumps(device_response, indent=4))