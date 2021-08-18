import requests
import json

showcmd = {
    "ins_api": {
        "version":"1.0",
        "type":"cli_show"
    }
}

print(type(showcmd))
print(json.dumps(showcmd, indent=4))
print(type(json.dumps(showcmd, indent=4)))
