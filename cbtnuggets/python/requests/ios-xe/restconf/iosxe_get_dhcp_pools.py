import requests
import json
from routers import router1

def main():
    requests.packages.urllib3.disable_warnings()
    api_path = f"https://{router1['HOST']}:{router1['PORT']}/restconf"
    auth = (f"{router1['USER']}", f"{router1['PASS']}")
    headers = {
        "Accept":"application/yang-data+json"
    }

    dhcp_response = requests.get(f"{api_path}/data/Cisco-IOS-XE-native:native/ip/dhcp/pool", headers=headers,
                                auth=auth, verify=False)
    
    print(dhcp_response.status_code)
    if dhcp_response.status_code == 200 and dhcp_response.text:
        print(json.dumps(dhcp_response.json(), indent=3))
    else:
        print("No DHCP pools configured")

if __name__ == "__main__":
    main()