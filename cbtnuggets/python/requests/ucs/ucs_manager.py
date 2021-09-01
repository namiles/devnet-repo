from ucsmsdk.ucshandle import UcsHandle
# help(UcsHandle)

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

#Reservation sandbox
handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")

handle.login()
# DOCUMENTATION https://github.com/CiscoUcs/ucsmsdk https://ucsmsdk.readthedocs.io/en/latest/

#ORG INFO
org = handle.query_classid(class_id="orgOrg", hierarchy=True)
print(org)

# Server Blade info
servers = handle.query_classid("computeBlade")

# print(srv)
for server in servers:
    print(server)

for server in servers:
    print(server.dn, server.num_of_cpus, server.available_memory)

# Specific DN query
blade = handle.query_dn('sys/chassis-3/blade-1')
print(blade)

# Logout
handle.logout()

