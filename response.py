import requests
import sys

def fetch_url (username):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    status = response.status_code
    if (status == 404):
        print("The page/endpoint doesn't exist.")
        sys.exit()
    if (status != 200):
        print("Something went wrong while fetching the api.")
        sys.exit()
    if (status == 200):     
        return response.json()
    print("Something went wrong.")
    sys.exit()

def fetch_commit_message(repo, hash):
    # /username/repo change to /repo only because repo_name automatically adds username/repo when the api is called.
    url = f'https://api.github.com/repos/{repo}/commits/{hash}'
    response = requests.get(url)
    status = response.status_code
    if (status == 404):
        print("The page/endpoint doesn't exist.")
        sys.exit()
    if (status != 200):
        print("Something went wrong while fetching the api.")
        sys.exit()
    if (status == 200):     
        return response.json()['commit']['message']
    print("Something went wrong.")
    sys.exit()