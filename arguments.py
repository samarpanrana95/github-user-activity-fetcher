def check_length (arguments):
    if len(arguments) != 2:
        return False
    return True

def check_username_validity (arguments):
    username = arguments[1]
    
    # Github prohibits the use of symbols in usernames
    prohibited_letters = ['@', '!', '$', '#', '*', '+', '.']
    for letter in prohibited_letters:
        if letter in username:
            return False

    # Github prohibits the use of letters outside of ascii characters such as Latin é in usernames
    if (username.isascii() == False):
        return False

    # Github prohibits the use of hyphen as the first and last letters in usernames
    if (username.startswith('-') == True or username.endswith('-') == True):
            return False
    
    return True