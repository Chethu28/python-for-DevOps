# GitHub Pull Request Counter

###This Python script retrieves information about pull requests from the GitHub API and counts the number of pull requests created by each user.

import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Make the request to the GitHub API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    pull_requests = response.json()

    pr_creators = {}

    # Count the number of pull requests for each creator
    for pr in pull_requests:
        creator = pr['user']['login']
        pr_creators[creator] = pr_creators.get(creator, 0) + 1

    # Print the dictionary containing creator and PR count
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    # Print an error message if the request was not successful
    print(f"Error: Unable to fetch pull requests. Status code: {response.status_code}")
