import requests
import json

token = 'NjNjNjVjODctM2Q1Ny00ZTc1LTk0YzUtMDgxYWMwNjExYzdhZGVjZWVjZjUtMDEx_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
room_url = 'https://api.ciscospark.com/v1/rooms'

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

print('\n', roomId)

'''
Posting Messages
'''
msg_url = 'https://api.ciscospark.com/v1/messages'
msg_payload = {
    'roomId':roomId,
    'text':'ALERT: This was posted to this room using the roomId and Python requests library!'
}
msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_payload)).json()
print(json.dumps(msg_response))

# for x in range(1,21):
#     msg_payload = {
#         'roomId':roomId,
#         'text':f'ALERT: {x}'
#     }
#     msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_payload)).json()