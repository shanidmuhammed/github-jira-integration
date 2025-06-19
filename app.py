from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def createJira():
    url = "https://your-domain.atlassian.net/rest/api/3/issue"
    token = ""
    auth = HTTPBasicAuth("your-email@example.com", token)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": {"key": "SCRUM"},
            "summary": "",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": "",
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "issuetype": {"id": "10001"},
            # "priority": {"name": "High"},
            "labels": ["bug", "ui"]
        }
    }

    response = requests.request(
    "POST",
    url,
    data=json.dumps(payload),
    headers=headers,
    auth=auth
    )
    return response.text

app.run(host='0.0.0.0')
