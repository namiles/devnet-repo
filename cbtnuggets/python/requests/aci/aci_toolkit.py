#acitoolkit.readthedocs.io
from acitoolkit.acitoolkit import *

# See capabilities
# dir()

url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = '!v3G@!4@Y'

# Create the session object
session = Session(url, user, pw)

# Login to the session
session.login()

# Get tenants
tenants = Tenant.get(session)
for tenant in tenants:
    print('Tenant name:',tenant.name)
    print('Tenant Desc:',tenant.descr)
    print('*' * 30)
    print(' ')

# Create a new Tenant
new_tenant = Tenant("nick_python_tenant")

# Create the application profile and the EPG
anp = AppProfile('Nicks_app', new_tenant)
epg = EPG('Nicks_epg', anp)

# Create the L3 Namespace
# Parent of context and bridge domain is the tenant
context = Context('Nicks_VRF', new_tenant)
bridge_domain = BridgeDomain('Nicks_bd', new_tenant)

# Context --> Bridge Domains --> EPG --> AP --> Tenant

# Associate the BD with the L3 Namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

##### Tenant Creation is completed #####
print(new_tenant.get_url())
print(new_tenant.get_json())
response = session.push_to_apic(new_tenant.get_url(), data=new_tenant.get_json())
print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    print('Tenant name:',tenant.name)
    print('Tenant Desc:',tenant.descr)
    print('*' * 30)
    print(' ')

# app_profiles = AppProfile.get(session, new_tenant)
# print(app_profiles[0])

# new_tenant.mark_as_deleted()
# session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())