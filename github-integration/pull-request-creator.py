# GitHub Pull Request Counter

###This Python script retrieves information about pull requests from the GitHub API.

import requests

api_url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Make the request to the GitHub API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    pull_requests = response.json()

    # Print information about each pull request creator
    for pr in pull_requests:
        creator_login = pr['user']['login']
        creator_url = pr['user']['id']
        print(f"Creator: {creator_login}, Creator ID: {creator_url}")
else:
    # Print an error message if the request was not successful
    print(f"Error: Unable to fetch pull requests. Status code: {response.status_code}")
