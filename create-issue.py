# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sqlonlinux.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("sqlonlinux@gmail.com", "ATATT3xFfGF0B0zAbZ2vNQ-y7srBrGQWoZSWR8zgvLHD1cJwklbNcEGdnHBuFNOuq6kRT6fed2LpYLKSmeWkbsYxp7vb-M0KW8Z1b_O0ihyMid4kdpNPBrs4hgV2GXQ_Z1cYkHvHy5HmQeEZ0R1w5GyfZfev0Q-8s5UL-Az2EcQsp32-ctSNA2U=589E62A2")

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