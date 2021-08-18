import meraki

X_CISCO_MERAKI_API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0" #read-only sandbox key

# Create new client connection
dashboard = meraki.DashboardAPI(X_CISCO_MERAKI_API_KEY)

# Get list of orgs
orgs = dashboard.organizations.getOrganizations()
for org in orgs:
    print(f"Org ID: {org['id']}, Org name: {org['name']}")

print()

# Get list of networks in devent sandbox org
networks = dashboard.organizations.getOrganizationNetworks("549236")
for net in networks:
    print(f"Network ID: {net['id']}, Network name: {net['name']}")

print()

# Get devices in devnet sandbox network
devices = dashboard.networks.getNetworkDevices("L_646829496481105433")
for dev in devices:
    print(f"Device model: {dev['model']}, Device serial: {dev['serial']}, Device MAC: {dev['mac']}")