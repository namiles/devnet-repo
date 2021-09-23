from ncclient import manager
import xml.dom.minidom
import xmltodict
import pprint
import sys
from routers import router1

def main():

    netconf_filter = open("interfaces_filter.xml").read()

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

        #Get interface data using get with netconf filter
        interface_netconf = m.get(netconf_filter) # uses the <get> netconf RPC
        # print() #spacing
        # print('Type of interface config:', type(interface_netconf))
        # xml_doc = xml.dom.minidom.parseString(str(interface_netconf))
        # print('Type of xml_doc after parsing with xml.dom.minidom: ', type(xml_doc))
        # print() #spacing
        # print(xml_doc.toprettyxml(indent="   "))

        print('*' * 100, '\n')

        #Use XMLtodict to convert the interface data to parsible dict
        interface_dict = xmltodict.parse(interface_netconf.xml)['rpc-reply']['data'] #have to add on .xml
        print(type(interface_dict))
        pprint.pprint(interface_dict)

        print('\n', '*' * 100, '\n', sep="")

        name = interface_dict['interfaces']['interface']['name']['#text'] #have to use #text key to get the name of interface
        print('Hostname:', name)

        print('\n', '*' * 100, '\n', sep="")
        
        config = interface_dict['interfaces']['interface']
        operational_state = interface_dict['interfaces-state']['interface']

        print(f"Data for {config['name']['#text']}")
        print(f"Name: {config['name']['#text']}")
        print(f"Description: {config['description']}")
        print(f"Enabled?: {config['enabled']}")
        print(f"Packets In: {operational_state['statistics']['in-unicast-pkts']}")

        print('\n', '*' * 100, '\n', sep="")

if __name__ == '__main__':
    sys.exit(main())