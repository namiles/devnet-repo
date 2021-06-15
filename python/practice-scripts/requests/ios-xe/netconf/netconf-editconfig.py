from ncclient import manager
import xml.dom.minidom
import xmltodict
import pprint
import sys
from routers import router1

def main():

    netconf_filter = open("interfaces_filter.xml").read()
    netconf_config_template = open("interfaces_config.xml").read()
    netconf_config = netconf_config_template.format(interface_name="GigabitEthernet2", interface_desc="Network Interface")

    # Connects using the NETCONF protocol
    with manager.connect(host=router1['HOST'], port=router1['PORT'], username=router1['USER'],
                         password=router1['PASS'], hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        device_reply = m.edit_config(netconf_config, target="running")
        print(device_reply)

        #Get interface data using get with netconf filter
        interface_netconf = m.get(netconf_filter)

        #Use XMLtodict to convert the interface data to parsible dict
        interface_dict = xmltodict.parse(interface_netconf.xml)['rpc-reply']['data'] #have to add on .xml
        
        #create objects for config and op state data
        config = interface_dict['interfaces']['interface']
        operational_state = interface_dict['interfaces-state']['interface']

        print('\n', '*' * 100, '\n', sep="")
        print('Start Data')
        print(f"Name: {config['name']['#text']}")
        print(f"Description: {config['description']}")
        print(f"Packets In: {operational_state['statistics']['in-unicast-pkts']}")
        print('\n', '*' * 100, '\n', sep="")

if __name__ == '__main__':
    sys.exit(main())