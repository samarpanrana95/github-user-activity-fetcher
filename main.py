import sys
from arguments import check_length, check_username_validity

all_arguments = sys.argv
if (check_length(all_arguments) == False):
    print('Please provide a correct syntax. The syntax is github-activity <username>') 
    sys.exit()
if (check_username_validity(all_arguments) == False):
    print('Please provide a correct and valid username.') 
    sys.exit()
