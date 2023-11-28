# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sqlonlinux.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("sqlonlinux@gmail.com", "<API-Token")

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
              "text": "My first JIRA ticket - Pavan",
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
    
   
    
    "summary": "First JIRA Ticket",
    
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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
