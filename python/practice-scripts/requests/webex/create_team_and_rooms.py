import requests
import json

'''
Token retrieves from developer.cisco.com in "Getting Started" section
Lasts 12 hours
'''
token = 'NjNjNjVjODctM2Q1Ny00ZTc1LTk0YzUtMDgxYWMwNjExYzdhZGVjZWVjZjUtMDEx_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3'

# Creating a Team via Rest API
url = 'https://api.ciscospark.com/v1/teams'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

payload = {
    'name':'Devnet Pupils'
}

# post_response = requests.post(url, data=json.dumps(payload), headers=headers).json()
# print(json.dumps(post_response, indent=4))

get_response = requests.get(url, headers=headers).json()
teams = get_response['items']
for team in teams:
    if team['name'] == 'Devnet Pupils':
        teamId = team['id']
print('Devnet Pupils team ID:', teamId, '\n')


'''
Creating a Room
'''
room_url = 'https://api.ciscospark.com/v1/rooms'
# room_payload = {
#     'title':'Automating Webex Section',
#     'teamId':teamId
# }
# room_response = requests.post(room_url, headers=headers, data=json.dumps(room_payload)).json()
# print(json.dumps(room_response, indent=4), '\n')

for x in range(1,11):
    room_payload = {
        'title':f'Room #{x}',
        'teamId':teamId
    }
    room_response = requests.post(room_url, headers=headers, data=json.dumps(room_payload)).json()
    print(json.dumps(room_response, indent=4), '\n')
    


'''
Get Room ID
'''
# get_rooms = requests.get(room_url, headers=headers).json()
# print(json.dumps(get_rooms, indent=4), '\n')
# rooms = get_rooms['items']
# for room in rooms:
#     print(room['title'])
#     if room['title'] == 'Automating Webex Section':
#         roomId = room['id']




