from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='NWFmZjM2Y2MtODA5ZC00NTkwLThiMjYtZmM5ZmNmMTFlZjUwMzQ2ZGYwYWMtNWRj_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3')

members = api.memberships.list("Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMmUxN2U2ZDAtMGFhNi0xMWVjLWI5ZDctNzNhYmEyOGVhOGE1")
for member in members:
    print(member)