from acitoolkit.acitoolkit import *

# Always-On DevNet Sandbox credentials (at time of writing)
url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = '!v3G@!4@Y'

# Create the session object
session = Session(url, user, pw)
session.login()

tenant_list = Tenant.get(session)
for tenant in tenant_list:
    print(tenant)