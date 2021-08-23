from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")
handle.login()

lan_cloud = handle.query_classid("FabricLanCloud")
vlans = ["200", "201", "202"]

for vlan in vlans:
  vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan"+vlan, id=vlan)
  handle.add_mo(vlan_mo, modify_present=True) #Could also just use true and let python handle args

'''
Objects can continually be added to the handle and a single commit will commit them all
This is known as a "transaction", but comes with a few cavets:
 - if one object fails to be created, everything up to that point is rolled back and nothing is created
 - objects in the transaction cannot have dependencies on each other
 - Objects onyl become visible to other users if of UCS manager when the transaction is compelte
'''
handle.commit()

handle.logout()