import requests
import json
from webex_urls import webex_urls

'''
Token retrieves from developer.cisco.com in "Getting Started" section
Lasts 12 hours
'''
token = "NWFmZjM2Y2MtODA5ZC00NTkwLThiMjYtZmM5ZmNmMTFlZjUwMzQ2ZGYwYWMtNWRj_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3"

# Creating a Team via Rest API
url = webex_urls['teams_url']
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

payload = {
    'name':'Exam Tonight'
}

# post_response = requests.post(url, data=json.dumps(payload), headers=headers).json()
# print(json.dumps(post_response, indent=4))

get_response = requests.get(url, headers=headers).json()
teams = get_response['items']
for team in teams:
    if team['name'] == 'Exam Tonight':
        teamId = team['id']
print('Exam Tonight team ID:', teamId, '\n')


'''
Creating a Room
'''
room_url = webex_urls['rooms_url']
room_payload = {
    'title':'Practicing for exam tonight3',
    # 'teamId':teamId
}
room_response = requests.post(room_url, headers=headers, data=json.dumps(room_payload)).json()
print(json.dumps(room_response, indent=4), '\n')

# for x in range(1,11):
#     room_payload = {
#         'title':f'Room #{x}',
#         'teamId':teamId
#     }
#     room_response = requests.post(room_url, headers=headers, data=json.dumps(room_payload)).json()
#     print(json.dumps(room_response, indent=4), '\n')
    


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




