from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route("/jira", methods=['POST'])
def createjira():
    # Jira API endpoint URL
    url = "https://YOUR_JIRA_INSTANCE.atlassian.net/rest/api/3/issue"

    # Your Jira API token
    api_token = "YOUR_JIRA_API_TOKEN"

    # Authentication using email and API token
    auth = HTTPBasicAuth("chethanreddy.mp@gmail.com", api_token)

    # Headers for the HTTP request
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # JSON payload for creating a Jira issue
    payload = json.dumps({
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
    })

    # Get JSON data from the incoming request
    data_request = request.json

    # Check if the comment body is "/jira"
    if 'comment' in data_request and 'body' in data_request['comment'] and data_request['comment']['body'] == '/jira':
        # Make a POST request to create a Jira issue
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        # Return the response as JSON with formatting
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        # Return an error message if the condition is not met
        return json.dumps({"error": "Invalid comment for creating Jira issue"})


if __name__ == '__main__':
    # Run the Flask app on IP 0.0.0.0 and port 5000
    app.run("0.0.0.0", port=5000)
