'''

String formatting
- old way using %i, %s, %f, etc.
- new way using f strings

'''

print()

print("String formarring using old way - %")
print("-----------------------------------------------------")
# Old way using %
# This method is not ideal because code readability suffers with long code.
name = 'GNS3'
language = 'Python'
cost = 0
message1 = 'Hello %s community, it\'s time to start learning %s. This course costs $%i, or $%f if you prefer.' % (name, language, cost, cost)
print(message1)

print()

print("String formarring using .format")
print("-----------------------------------------------------")
# newer way using str.format()
dns = "8.8.8.8"
vrf = "Internet"
ping = 'ping' + ' '+ dns + ' ' + 'vrf' + ' ' + vrf
print(ping)
ping1 = 'ping {} vrf {}'.format(dns,vrf)
print(ping1)
ping2 = 'ping {} vef {}'
print(ping2.format(dns, vrf))

print()

print("String formarring using f strings, or string literals")
print("-----------------------------------------------------")
# String interpolation/f-string (python 3.6+)
# Lets you embed python expressions inside strings
name = 'nick'
a = 5
b = 5
print(f'Hello, {name}')
print(f'Five plus ten is {a+b}')

print()
