import requests

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Content-Type': 'application/json',
  # devnetuser:Cisco123! encoded
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
