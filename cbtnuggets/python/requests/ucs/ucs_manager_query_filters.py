from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")
handle.login()

# blades = handle.query_classid("computeBlade")
# for blade in blades:
#   print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)

#Filters for a models the equeal 'UCSB-EX-M4-1'
blades = handle.query_classid("computeBlade", filter_str="(model, 'UCSB-EX-M4-1', type='eq')")
for blade in blades:
  print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)

#Can also filter using regular expressions
# blades = handle.query_classid("computeBlade", filter_str="(dn, 'blade-[2,4,6,8]', type='re')")
# for blade in blades:
#   print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)

handle.logout()