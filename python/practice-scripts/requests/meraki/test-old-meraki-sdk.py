from meraki_sdk.meraki_sdk_client import MerakiSdkClient
# This SDK is deprecated in favor of 'meraki' package

X_CISCO_MERAKI_API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0" #read-only sandbox key

# Create new client connection
dashboard = MerakiSdkClient(X_CISCO_MERAKI_API_KEY)

# Get list of orgs
orgs = dashboard.organizations.get_organizations()
for org in orgs:
    print(f"Org ID: {org['id']} and Org name: {org['name']}")

PARAMS={}
PARAMS["organization_id"] = "549236"
print(PARAMS)

print()

# Get list of networks in devent sandbox org
networks = dashboard.networks.get_organization_networks(PARAMS)
for net in networks:
    print(f"Network ID: {net['id']}, Network name: {net['name']}")

print()

# Get devices in devnet sandbox network
devices = dashboard.devices.get_network_devices("L_646829496481105433")
for dev in devices:
    print(f"Device model: {dev['model']}, Device serial: {dev['serial']}, Device MAC: {dev['mac']}")