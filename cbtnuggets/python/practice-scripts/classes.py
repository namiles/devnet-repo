import modules

# class Router:
#     '''Class used to describe routers'''
#     def __init__(self, model, swversion, ip_address, location): # double underscore methods are known as dunder/magic method
#         '''intilaizing values'''
#         self.model = model
#         self.swversion = swversion
#         self.ip_address = ip_address
#         self.location = location

#     def getInfo(self):
#         '''Returns information about router'''
#         info =  f'Router Model:       {self.model}\n'\
#                 f'Software Version:   {self.swversion}\n'\
#                 f'IP Address:         {self.ip_address}\n'\
#                 f'Location:           {self.location}'
#         return info

# class Switch(Router):
#     def getInfo(self):
#         '''Returns information about Switch'''
#         info =  f'Switch Model:       {self.model}\n'\
#                 f'Software Version:   {self.swversion}\n'\
#                 f'IP Address:         {self.ip_address}\n'\
#                 f'Location:           {self.location}'
#         return info


print()

r1 = modules.Router("Cisco 2911","15.6.7","10.1.1.135","Rack 24")
print(r1.getInfo())
print()
r2 = modules.Router("Cisco 1911", "12.2","10.1.1.136","Rack 25")
print(r2.getInfo())

print()
s1 = modules.Switch("Cisco Catalyst 3750","16.1","10.1.1.137","Rack 28")
print(s1)
print(s1.getInfo())
s1.set_ip_address('192.168.200.120')
print('Updated IP address:')
print(s1.getInfo())

print()

print(dir(modules.Router))

print()


