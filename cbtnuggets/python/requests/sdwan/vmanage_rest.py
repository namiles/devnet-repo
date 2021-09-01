import requests
import json
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)

    def login(vmanage_ip, username, password):
        '''Login and authenticate with vManage'''
        base_url_str = f'https://{vmanage_ip}:443/'
        login_action = '/j_security_check'

        # Format data for loginForm
        login_data = {
            'j_username' : username, 
            'j_password' : password
        }

        # Url for posting login data
        login_url = base_url_str + login_action

        sess = requests.session()
        # If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False)

        if not login_response.ok or login_response.text:
            print('login failed')
            sys.exit(1)
        else:
            print('log in successful\n')

    def get_request(vmanage_ip, mount_point):
        '''
        Perform a GET Request.
        
        Takes the mount point as an argument.

        For example to list devices, pass in "devices"
        '''
        url = f'https://{vmanage_ip}:443/dataservice/{mount_point}'

        response = requests.request("GET", url, verify=False)
        data = response.json()['data']
        return data

    def post_request(vmanage_ip, mount_point, payload, headers={'Content-Type': 'application/json'}):
        '''Perform a POST'''
        url = f'https://{vmanage_ip}:443/dataservice/{mount_point}'
        payload = json.dumps(payload)

        response = requests.request("POST", url, data=payload, headers=headers, verify=False)
        data = response.json()['data']
        return data

def main():
    #DevNet Always-on SD-WAN Sandbox
    vmanage = rest_api_lib("131.226.217.141", "devnetuser", 'RG!_Yw919_83')
    devices = vmanage.get_request("devices")
    print(json.dumps(devices, indent=4))

if __name__ == "__main__":
    main()
