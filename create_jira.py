# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])

def createJira():

    url = "https://sqlonlinux.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF03dzrNOTG6lngkmO8iWr_CSIE1hchKOMAyNAbIWBC9Hbu4jtlnEQmkOzZ_R0jfvlX9wCjjwFIU3Ndua-UmEdJuiCSC4C1ySpixiu9cav71b_aIXsmIb96vco1cD1Z4-oxfqf-YGCEJq3wPnGQX_NcsJdNBxSgUFlwkUvIr0uAW8E=3B980958"
    auth = HTTPBasicAuth("sqlonlinux@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "My first JIRA ticket - Pavan - GitHub and JIRA Integration",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "SCRUM"
        },
        "issuetype": {
            "id": "10001"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

  
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)