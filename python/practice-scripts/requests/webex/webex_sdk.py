from webexteamssdk import WebexTeamsAPI
from webexteamssdk.api import people

api = WebexTeamsAPI(access_token='YzkxMzU2NjMtZWMyMy00ZTJhLThmNWYtM2EzZWUzYjE5ZDg0ZjUwMDQzYWYtNWEw_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3')

'''
Team Info
'''
teams = api.teams.list() #return as team class objects, not JSON data
for team in teams:
    print(team)
    if getattr(team, 'name') == 'Devnet Pupils': # getattr can be used to get details about the class object
        teamId = team.id #can also use decimal notation
        print(teamId)

'''
People
'''
print(api.people.me())
emails = [
    'nick@nickmiles.me'
]
api.people.create(emails=emails, displayName='Nick Test', firstName='Nick', lastName='Test') # only email is required
print(api.people.get(email='nick@nickmiles.me'))
