import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://<EMAIL>.atlassian.net/rest/api/3/issue"

api_token=""

auth = HTTPBasicAuth("<EMAIL>", api_token)

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
              "text": "my jira ticket",
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
      "id": "10003"
    },
    "summary": "first jira ticket",
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