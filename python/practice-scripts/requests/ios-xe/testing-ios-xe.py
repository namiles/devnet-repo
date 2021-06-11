from re import S
from ncclient import manager
import xml.dom.minidom
import xmltodict
import pprint
import sys

HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your IOS-XE device
PORT = 10000
# use the user credentials for your IOS-XE device
USER = 'developer'
PASS = 'C1sco12345'

netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces-state>
</filter>
"""

def main():
    # Connects using the NETCONF protocol
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # # print all NETCONF capabilities
        # for capability in m.server_capabilities:
        #     print(capability.split('?')[0])
        #     #get command gets operational or config data
        
        # print('*' * 100, '\n')

        #Get interface data using get with netconf filter
        interface_netconf = m.get(netconf_filter)
        print(type(interface_netconf))
        print()
        xml_doc = xml.dom.minidom.parseString(str(interface_netconf))
        print(type(xml_doc))
        print(xml_doc.toprettyxml(indent="   "))

        print('*' * 100, '\n')

        #Use XMLtodict to convert the interface data to parsible didct
        interface_dict = xmltodict.parse(interface_netconf.xml)['rpc-reply']['data']
        print(type(interface_dict))
        pprint.pprint(interface_dict)

        print('\n', '*' * 100, '\n', sep="")

        name = interface_dict['interfaces']['interface']['name']['#text']
        print('Hostname:', name)

        print('\n', '*' * 100, '\n', sep="")
        
        config = interface_dict['interfaces']['interface']
        op_state = interface_dict['interfaces-state']['interface']

        print('Start Data')
        print(f"Name: {config['name']['#text']}")
        print(f"Description: {config['description']}")
        print(f"Packets In: {op_state['statistics']['in-unicast-pkts']}")

        print('\n', '*' * 100, '\n', sep="")

if __name__ == '__main__':
    sys.exit(main())