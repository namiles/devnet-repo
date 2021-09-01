import xmltodict

# XML
print("#--------------- Working with XML ---------------#")
print()

# Working with XML natively is confusing with Python and can be hard to grasp.
# xmltodict is a module that can be used to convert XML to a special dictinary that does not allow elements to change order
# Order DOES MATTER in XML

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