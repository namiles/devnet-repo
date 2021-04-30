

#Classes are defined starting with the Class keyword
print()

class Router:
    '''Class used to describe routers'''
    def __init__(self, model, swversion, ip_address, location): # double underscore methods are known as dunder/magic method
        '''intilaizing values'''
        self.model = model
        self.swversion = swversion
        self.ip_address = ip_address
        self.location = location

    def getInfo(self):
        '''Returns information about router'''
        info =  f'Router Model:       {self.model}\n'\
                f'Software Version:   {self.swversion}\n'\
                f'IP Address:         {self.ip_address}\n'\
                f'Location:           {self.location}'
        return info

class Switch(Router):
    def getInfo(self):
        '''Returns information about Switch'''
        info =  f'Switch Model:       {self.model}\n'\
                f'Software Version:   {self.swversion}\n'\
                f'IP Address:         {self.ip_address}\n'\
                f'Location:           {self.location}'
        return info

r1 = Router("Cisco 2911","15.6.7","10.1.1.135","Rack 24")
print(r1.getInfo())
print()
r2 = Router("Cisco 1911", "12.2","10.1.1.136","Rack 25")
print(r2.getInfo())

print()
s1 = Switch("Cisco Catalyst 3750","16.1","10.1.1.137","Rack 28")
print(s1.getInfo())


print()

