from ncclient import manager
import xmltodict
import pprint
import sys
from routers import router1

def main():
    # Connects using the NETCONF protocol
    with manager.connect(
        host=router1['HOST'], 
        port=router1['PORT'], 
        username=router1['USER'],
        password=router1['PASS'],
        hostkey_verify=False,
        device_params={'name': 'default'},
        look_for_keys=False, 
        allow_agent=False) as m:

        print('\n', '*' * 100, '\n', sep="")

        running_config = m.get_config(source='running')
        print(running_config)
        print(type(running_config))

        print('\n', '*' * 100, '\n', sep="")

        running_config_dict = xmltodict.parse(running_config.xml)['rpc-reply']['data']
        print(type(running_config_dict))
        pprint.pprint(running_config_dict)

        print('\n', '*' * 100, '\n', sep="")

if __name__ == '__main__':
    sys.exit(main())