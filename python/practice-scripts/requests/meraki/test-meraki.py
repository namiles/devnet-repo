import meraki
X_CISCO_MERAKI_API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
dashboard = meraki.DashboardAPI(X_CISCO_MERAKI_API_KEY)
organizationsList = dashboard.organizations.getOrganizations()

print()

for org in organizationsList:
    if(org['id'] == '549236'):
        devnet_org_id = org['id']
        devnet_org = org
        print('Entire devnet org object:', org)
    
print('Devnet Sandbox organization ID:', devnet_org['id'])

print()

#get networks in an organization
devnet_org_networks = dashboard.organizations.getOrganizationNetworks(devnet_org_id)
print(devnet_org_networks)

print()

#get devices in a specific network ID
devnet_network_devices = dashboard.networks.getNetworkDevices('L_646829496481105433')
print(devnet_network_devices)
print()

serial = 'Q2HP-F5K5-R88R'

#get device info using serial #
print(dashboard.devices.getDevice(serial))

print()

#update device - forbidden for meraki read-only sandbox
# response = dashboard.devices.updateDevice(
#     serial,
#     name='Nick\'s AP'
# )