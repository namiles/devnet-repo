from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")
handle.login()

'''
To Delete or remove UCS Manager objects, query for the object and add the removal of the 
object to the handle with the remove_mo() method.
'''
vlans = handle.query_classid("FabricVlan")

for vlan_mo in vlans:
    if vlan_mo.id != "1":
        handle.remove_mo(vlan_mo)

handle.commit()
handle.logout()