import requests
import json

url = "https://swapi.dev/api/people/5/"

payload={}
headers = {}

response = requests.get(url, headers=headers, data=payload)

print()

print(response.text)
print('Response type:', type(response))
print('Status code:', response.status_code)
print('Headers:', response.headers)
print('Headers type: ', type(response.headers))
print('URL:', response.url)
print('Encoding:', response.encoding)


print()

response_json = response.json()
print(type(response_json))
print(response_json['name'], '\'s ', 'birth year is ', response_json['birth_year'], sep="")

print()

response_json_formatted = json.dumps(response_json, indent=2)
print(type(response_json_formatted))
print(response_json_formatted)