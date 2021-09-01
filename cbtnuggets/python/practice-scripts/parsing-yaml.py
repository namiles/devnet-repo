import yaml

# YAML
print("#--------------- Working with YAML ---------------#")
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
print('Dict after change:',yaml_dict)
print()

#Writing back to file
with open("interfaces.yaml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))