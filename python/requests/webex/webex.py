import requests
import json
from webex_urls import webex_urls

token = "OTJmZmI2MzctZDRmNS00OWE1LTgwNDktMDk0YmE1N2ViNThjNjgwYTU3MTgtNDY4_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3"

'''
Organizations
'''
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
org_response = requests.get(webex_urls['organizations_url'], headers=headers).json()['items']
print("\n----- Organizations -----")
for org in org_response:
    print(org)

'''
Teams
'''
teams_response = requests.get(webex_urls['teams_url'], headers=headers).json()['items']
print("\n----- Teams -----")
for team in teams_response:
    print('Team Name:', team['name'], 'Id:', team['id'])

'''
Rooms
'''
rooms_response = requests.get(webex_urls['rooms_url'], headers=headers).json()['items']
print("\n----- Rooms -----")
for room in rooms_response:
    print('Title:', room['title'])

'''
Memberships
'''
members_response = requests.get(webex_urls['memberships_url'], headers=headers).json()['items']
print("\n----- Memberships -----")
for member in members_response:
    print(member['personDisplayName'], 'is a member of room', member['roomId'])