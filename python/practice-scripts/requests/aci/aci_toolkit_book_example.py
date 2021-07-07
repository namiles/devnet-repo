import sys
import acitoolkit.acitoolkit as aci

apic_url = "https://sandboxapicdc.cisco.com"
username = "admin"
password = "ciscopsdt"

# Login to APIC
session = aci.Session(apic_url, username, password)
RESP = session.login()
if not RESP.ok:
    print("Could not login to APIC Controller")
    sys.exit()

endpoints = aci.Endpoint.get(session)
print('{0:19s}{1:14s}{2:20s}{3:8s}{4:17s}{5:10s}'.format(
    "MAC_ADDRESS",
    "IP ADDRESS",
    "ENCAP",
    "TENANT",
    "APP_PROFILE",
    "EPG"
))
print('-'*82)

for ep in endpoints:
    epg = ep.get_parent() #every endpoint has an endpoint group parent
    app_profile = epg.get_parent() #every endpoint group has an AP parent
    tenant = app_profile.get_parent() #every AP has a tenant parent
    print('{0:19s}{1:14s}{2:20s}{3:8s}{4:17s}{5:10s}'.format(
        ep.mac,
        ep.ip,
        ep.encap,
        tenant.name,
        app_profile.name,
        epg.name
    ))