# Classes are defined starting with the Class keyword
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

# Switch class is deribed from Router class
class Switch(Router):
    def getInfo(self):
        '''Returns information about Switch'''
        info =  f'Switch Model:       {self.model}\n'\
                f'Software Version:   {self.swversion}\n'\
                f'IP Address:         {self.ip_address}\n'\
                f'Location:           {self.location}'
        return info