import csv
import json
import xmltodict
import yaml
import os

'''
File input and output

Modes
- r = open for reading (default)
- w = open for writing (overwrites)
- x = open for exclusive creation, failing if the file already exsits
- a = Open for writing, appending to the file if it exists
- b = Open in binary mode
- t = Open in text mode (default)
- + = Open for updating (read and write)

'''


print(os.getcwd())

#-------------------------------------------------------------#

# Take file to open as a string and specify mode. readdata is an object created to store the contents of the file.
readdata = open("textfile.txt", "r")

# read() can be used to print contents
print()
print(readdata.read())
print()

# When using open(), you have to close the file:
readdata.close()

'''
Keep track of opening and closing files can be annoying.
Python provides the with statement, also called a context manager.
It uses the open() function but doesn't require assigning to an object and automatically closes the file.
'''

with open("textfile.txt", "r") as data:
    print(data.read())

# a+ can be used to write to the file by appending. 

with open("textfile.txt", "a+") as data:
    print(data.write("\nThis line was added using python."))


# Read file after adding the line.
with open("textfile.txt", "r") as data:
    print(data.read())
print()

#-------------------------------------------------------------#

print("#------------------------------Parsing Data-------------------------------#")
print()

'''
Parsing Data

CSV
- Each line in CSV represents a row, and commas are used to separate individual data fields to make it easier to parse.
- CSV module must be imported (import csv)

JSON
- Data structure derived from the Javascript programming language
- Can be used as a portable data structure for any programming language
- Build around key:value pairs.
- all keys must be surrounded by quotes
- JSON module must be imported (import json)

XML
- Natively supported by Python
- Common in configuration automation
- xmltodict can be used to convert XML to a python dictionary.
- This is a special dictionary because order does matter in XML. 

YAML
- Must install PyYaml module
- pip install PyYaml

'''

# CSV
print("-- Working with CSV --")
print()

samplefile = open("routers.csv") # open CSV file
samplereader = csv.reader(samplefile) # create reader object
sampledata = list(samplereader) # 
print("Data:", sampledata)
print()

print("Print first row:",sampledata[0])
print("Print data field in first row:",sampledata[0][0])
print("Print second row:",sampledata[1])
print("Print second data field in second row:",sampledata[1][1])
print()

# You can interate through CSVs using the with statement from previous examples
with open("routers.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]
        print(f"{device} is in {location.rstrip()} and has IP {ip}")
print()

# # Writing to a CSV file
# print("Please add a new router to the list.")
# hostname = input("Enter hostname: ")
# ip = input("Enter IP address: ")
# location = input("Enter location: ")

# # Create a list object
# newrouter = [hostname, ip, location]

# with open("routers.csv", "a") as data: #open for writing, appending to the file
#     csv_writer = csv.writer(data)
#     csv_writer.writerow(newrouter)


# JSON
print("-- Working with JSON --")
print()

'''
JSON Functions

load()  - Import native JSON and convert to python dictionary from a file
loads() - Import JSON data from a string for parsing and manipulating within program
dump()  - Write JSON data from Python object to a file
dumps() - Take JSON dictionary data and convert to a serialized string for parsing and manipulating

'''

with open("interfaces.json") as data:
    interfacedata = data.read()

#Print raw JSON data
print(interfacedata)

#Convert JSON data into a dictionary
interfaces_dict = json.loads(interfacedata)
print()

#Print interfaces dictionary
print(interfaces_dict)

#Modifying Data
interfaces_dict["interfaces"]["interface1"]["description"] = "Main uplink"
interfaces_dict["interfaces"]["interface2"]["description"] = "Backup uplink"
print()

#Print dictionary after updating data
print(interfaces_dict)

#Saving JSON data back to file
with open("interfaces.json", "w") as fh:
    json.dump(interfaces_dict, fh, indent=4) #indent is optional but helps with improving readability

print()

# XML
print("-- Working with XML --")
print()

# Working with XML natively is confusing with Python and can be hard to grasp.
# xmltodict is a module that can be used to convert XML to a special dictinary that does not allow elements to change order
# Order matters in XML

with open ("interfaces.xml") as data:
    xml_example = data.read()

#Print raw XML data
print(xml_example)

#Convert XML data to a dictionary using xmltodict
xml_dict = xmltodict.parse(xml_example)
print()

#Print XML Dict
print("XML dict: ",xml_dict)

#Modifying data
xml_dict["interfaces"]["interface1"]["description"] = "Modified main uplink"
print()

#Print modified XML
print("Modified XML:", xml_dict)

#Writing XML back to file
with open("interfaces.xml", "w") as data: # w to overwrite existing data
    data.write(xmltodict.unparse(xml_dict, pretty=True)) #pretty is optional but helps with human readabiltiy. XML does not care about whitespace.
    print("\nXML file updated")

print()

# YAML
print("-- Working with YAML --")
print()

with open("interfaces.yaml") as data:
    yaml_sample = data.read()

#Print raw YAML data
print(yaml_sample)
print("Type of raw YAML data:",type(yaml_sample))

#Convert YAML to dict
yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)
print()

#Print Yaml dict
print(yaml_dict)
print("Type after converting:",type(yaml_dict))
print()

#Modifying Data
yaml_dict["interfaces"]["interface1"]["description"] = "Modified main uplink"
yaml_dict["interfaces"]["interface2"]["description"] = "Modified backup uplink"

#Print Yaml dict after modifying
print(yaml_dict)
print()

#Writing back to file
with open("interfaces.yaml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))


#-------------------------------------------------------------#

