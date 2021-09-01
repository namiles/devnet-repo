import csv

# CSV
print("#--------------- Working with CSV ---------------#")
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