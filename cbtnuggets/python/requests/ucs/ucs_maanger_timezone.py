from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.comm.CommDateTime import CommDateTime
from ucsmsdk.mometa.comm.CommNtpProvider import CommNtpProvider

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

# DevNet Sandbox reservation lab
handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")
handle.login()

# Retrieve timezone info
timezone_mo = handle.query_dn("sys/svc-ext/datetime-svc")
print(timezone_mo)

# Set timezone
timezone_mo.timezone = 'America/Lima'
handle.set_mo(timezone_mo)
handle.commit()

# Retrieve timezone info again
timezone_mo = handle.query_dn("sys/svc-ext/datetime-svc")
print (timezone_mo)

#----#

# Retrieve NTP Servers
ntp_mos = handle.query_classid("CommNtpProvider")
# Should print an empty list
print(ntp_mos)

#Add NTP Server
timezone_mo = handle.query_dn("sys/svc-ext/datetime-svc")
ntp_mo = CommNtpProvider(parent_mo_or_dn=timezone_mo,name="10.10.10.20")
handle.add_mo(ntp_mo)
handle.commit()

#Retreive NTP server object and print
ntp_mos = handle.query_classid("CommNtpProvider")
for ntp_provider_mo in ntp_mos:
 print (ntp_provider_mo)

#Delete NTP Server
ntp_mo = handle.query_dn("sys/svc-ext/datetime-svc/ntp-10.10.10.20")
handle.remove_mo(ntp_mo)
handle.commit()

# Logout
handle.logout()