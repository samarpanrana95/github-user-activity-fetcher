import sys
from response import fetch_url, fetch_commit_message
from arguments import check_length, check_username_validity

all_arguments = sys.argv
if (check_length(all_arguments) == False):
    print('Please provide a correct syntax. The syntax is github-activity <username>') 
    sys.exit()
if (check_username_validity(all_arguments) == False):
    print('Please provide a correct and valid username.') 
    sys.exit()

username = all_arguments[1]
result = fetch_url(username)
for action in result:
    if (action['type'] == 'PushEvent'):
        repo_name = action['repo']['name']
        repo_url = action['repo']['url']
        repo_hash = action['payload']['head']
        message = fetch_commit_message(repo_name, repo_hash)
        print(f'- Pushed a commit to {repo_name}.\n{message}\nLink : {repo_url}\n')
    elif (action['type'] == 'CreateEvent'):
        repo_name = action['repo']['name']
        repo_url = action['repo']['url']
        repo_decsription = action['payload']['description']
        print(f'- Created a repo named {repo_name}.\n{repo_decsription}\nLink : {repo_url}\n')