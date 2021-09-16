import requests
import json

url = "https://webexapis.com/v1/messages"

payload = json.dumps({
  "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYTZlNzVlZjAtMTVjZS0xMWVjLWEzZGYtOWQ3MTBhZjI3ZGFl",
  "text": "Posted using python code generated from Postman"
})
headers = {
  'Authorization': 'Bearer ODE2NDFlZDEtYzU2MS00ZDk0LThiOTYtODU5MGY5ZDJhZmVmYmU3NzYwNTItNTcw_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
