import requests

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/auth/token"

payload={}
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
