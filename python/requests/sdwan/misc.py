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
#login post
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

# Get Devices
user_url = 'https://sandbox-sdwan-1.cisco.com/dataservice/admin/user'
user_response = session.get(user_url, verify=False).json()['data']
# print(json.dumps(device_response, indent=4))
for user in user_response:
    if user["userName"] == "devnetuser":
        print(user["description"])
        user["description"] = "hello changed with python"

print(json.dumps(user_response, indent=4))
post_user_response = session.post(user_url, data=json.dumps(user_response), verify=False)
print(post_user_response)