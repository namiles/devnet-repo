import requests
import json

print()

r = requests.get('https://swapi.dev/api/people/?page=2')
#print JSON of response object
print(r.json())
print(type(r))
print(r.headers['content-type'])
print(r.ok)
print()

starwars_data = r.json()
print(type(starwars_data))

starwars_formatted_data = json.dumps(r.json(), indent=2)
print()
print(starwars_formatted_data)
print()

