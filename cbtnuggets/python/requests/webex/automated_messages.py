import requests
import json
from webex_urls import webex_urls

token = 'NDA4MDE0ZTItZTE2MC00MGMwLTk3NWEtZGU0NjRkNTliOTBmYzIzNzlmNGYtNmM4_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
room_url = webex_urls['rooms_url']

'''
Get Room ID
'''
get_rooms = requests.get(room_url, headers=headers).json()
print(json.dumps(get_rooms, indent=4), '\n')
rooms = get_rooms['items']
for room in rooms:
    print(room['title'])
    if room['title'] == 'Automating Webex Section':
        roomId = room['id']
        break

print('\n', roomId)

'''
Posting Messages
'''
msg_url = webex_urls['messages_url']
msg_payload = {
    'roomId':roomId,
    'text':'ALERT: Testing URLS'
}
msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_payload)).json()
print(json.dumps(msg_response))

# for x in range(1,21):
#     msg_payload = {
#         'roomId':roomId,
#         'text':f'ALERT: {x}'
#     }
#     msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_payload)).json()


msg_payload = {
    'roomId':roomId,
    'text':f'ALERT: nmiles has pushed an update to master branch.'
}
msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_payload)).json()