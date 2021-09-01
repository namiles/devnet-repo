import requests
import json
import sys
from webex_urls import webex_urls

token = "OTJmZmI2MzctZDRmNS00OWE1LTgwNDktMDk0YmE1N2ViNThjNjgwYTU3MTgtNDY4_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3"
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
teams = requests.get(webex_urls['teams_url'], headers=headers).json()['items']
rooms = requests.get(webex_urls['rooms_url'], headers=headers).json()['items']

room_name = input('Room name: ')
team_name = input('Team to create room under: ')

for team in teams:
    if team['name'] == team_name:
        teamId = team['id']
        print('Team found')
        payload = {
            'title':room_name,
            'teamId':teamId
        }
        create_room_response = requests.post(webex_urls['rooms_url'], data=json.dumps(payload), headers=headers).json()
        print('Created room successfully.')
        sys.exit(0)
    else:
        print('No team of that name.')
        answer = input('Would you like to create the room without a team tied to it? (y/n): ')
        if answer == 'y':
            payload = {
                'title':room_name
            }
            create_room_response = requests.post(webex_urls['rooms_url'], data=json.dumps(payload), headers=headers).json()
            print('Created room successfully.')
            sys.exit(0)
        else:
            print('Could not create room. Exitin script.')
            sys.exit(1)