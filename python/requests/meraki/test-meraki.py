import meraki

X_CISCO_MERAKI_API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0" #read-only sandbox key
dashboard = meraki.DashboardAPI(X_CISCO_MERAKI_API_KEY)

print()

organizationsList = dashboard.organizations.getOrganizations()
for org in organizationsList:
    if(org['id'] == '549236'): #if id equals ID of offical devnet sandbox
        #Save Id of devnet sandbox organization
        devnet_org_id = org['id']
        devnet_org = org  
  
print('Devnet Sandbox organization ID:', devnet_org['id'])

print()

#get devnet org admins
devnet_org_admins_list = dashboard.organizations.getOrganizationAdmins(devnet_org_id)
print('Printing out admins for devnet organization..')
for admin in devnet_org_admins_list:
    print(admin['name'])

print()

#get networks in an organization
devnet_org_networks = dashboard.organizations.getOrganizationNetworks(devnet_org_id)
print(devnet_org_networks)

print()

for network in devnet_org_networks:
    if(network['name'] == 'DevNet Sandbox ALWAYS ON'):
        print('Devnet sandbox always on network id:', network['id'])
        devnet_network_id = network['id']

print()

#get devices in a specific network ID
devnet_network_devices = dashboard.networks.getNetworkDevices(devnet_network_id)
print(devnet_network_devices)
print()

serial = 'Q2HP-F5K5-R88R'

#get device info using serial #
print(dashboard.devices.getDevice(serial))

print()

# update device - forbidden for meraki read-only sandbox
# response = dashboard.devices.updateDevice(
#     serial,
#     name='Nick\'s AP'
# )