import requests
import json
from webex_urls import webex_urls

'''
Token retrieves from developer.cisco.com in "Getting Started" section
Lasts 12 hours
'''
token = "NDA4MDE0ZTItZTE2MC00MGMwLTk3NWEtZGU0NjRkNTliOTBmYzIzNzlmNGYtNmM4_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3"

url = webex_urls['rooms_url']
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

get_response = requests.get(url, headers=headers).json()
rooms = get_response['items']
for room in rooms:
    print(room['id'])
    print(room['title'])
    print()