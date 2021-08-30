import requests
import json

# DevNet Nexus 1 device reservation sandbox
url = "http://10.10.20.58:80/ins"
uname = "admin"
pw = "Cisco123"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int brief",
    "output_format": "json"
  }
})

headers = {
  'Content-Type': 'application/json',
}

response = requests.post(url, auth=(uname,pw), headers=headers, data=payload).json()
print(json.dumps(response, indent=2, sort_keys=True))
