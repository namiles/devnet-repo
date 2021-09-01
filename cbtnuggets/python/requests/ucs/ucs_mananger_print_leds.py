from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")
handle.login()

'''
UCS Manager has five query methods:
    query_classid - get objects from a single class
        Returns a list of objects, the list may contain zero objects

    query_classids - get objects from multiple classes
        Returns a dictionary where the classid is the key and a list of zero or more objects is the value

    query_dn - get a single object by Dn
        Returns zero or one object

    query_dns - get multiple objects by Dn
        Returns a dictionary where the Dn is the key and the object is the value. 
        If the dn does not exist the value for that key will be None
    
    query_children - get the children objects of a specific object
        Returns a list of zero or more objects
'''

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        print(compute_resource.dn, leds[0].oper_state) #will always be 0 because there is only one object in the list

handle.logout()