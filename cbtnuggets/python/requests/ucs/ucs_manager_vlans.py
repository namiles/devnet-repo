from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

'''
VLANs are simple objects to create and understanding how to create a VLAN allows you to understand
how to create any UCS manager object.

The process to creating a new UCS Manager object starts with knowing the dn of the parent object 
or retrieving the parent object, of the object you are creating.

The UCS Manager objects are arranged in a hierarchical model, when a new object is created it 
needs to be placed in the object model under its' parent.

VLAN objects typically reside under the Lan Cloud. You could specify the dn for the Lan Cloud 
but best practice would be to use a query to retrieve the Lan Cloud object.
'''

handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")
handle.login()

lan_cloud = handle.query_classid("FabricLanCloud")
vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan100", id="100")
handle.add_mo(vlan_mo, True)
'''
modify_present (second argument in add_mo, that is true) allows the add_mo() method to act like 
a set_mo() and update the object if it already exists. By default modify_present is False meaning 
that if add_mo() was being used to create an object that already exists then the add 
operation would fail.

Basically if vlan100 already existed, it would just update the name and id if it wasn't already
set. Without true, it would fail if vlan100 existed.
'''
handle.commit()

