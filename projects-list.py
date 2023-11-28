# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sqlonlinux.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("sqlonlinux@gmail.com", "ATATT3xFfGF0B0zAbZ2vNQ-y7srBrGQWoZSWR8zgvLHD1cJwklbNcEGdnHBuFNOuq6kRT6fed2LpYLKSmeWkbsYxp7vb-M0KW8Z1b_O0ihyMid4kdpNPBrs4hgV2GXQ_Z1cYkHvHy5HmQeEZ0R1w5GyfZfev0Q-8s5UL-Az2EcQsp32-ctSNA2U=589E62A2")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)