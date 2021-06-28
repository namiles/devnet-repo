from dnacentersdk import DNACenterAPI
import json

#Can use environment variables for base url and auth, refer to documentation.
api = DNACenterAPI(base_url='https://sandboxdnac2.cisco.com', 
                   username='devnetuser', 
                   password='Cisco123!')

#Get Devices
devices = api.devices.get_device_list()
for device in devices.response:
    print("Type:        ", device.type)
    print("Hostname:    ", device.hostname)
    print("IP Address:  ", device.managementIpAddress)
    print("ID:          ", device.id)
    print(" ")

print('\n','*' * 80, '\n')

#Get Specific Device
device = api.devices.get_device_by_id('a25646c1-5c3d-4f18-b158-0f689a255a03')
print(device)

print('\n','*' * 80, '\n')

#Clients
clients = api.clients.get_overall_client_health()
print(json.dumps(clients, indent=4))

print('\n','*' * 80, '\n')

#Networks
networks = api.networks.get_overall_network_health()
print(networks)

