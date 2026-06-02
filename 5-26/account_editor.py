#login/ account creator
#will include login function w/ forgot pass word and a sign up fuunction
import time

accounts = {"John": 4321, "Jane":2345, "Bob":7890}

def window(username, accounts):
    logout_words = ["log out","logout"]
    passwd_words = ["password", "pass word"]

    welcome_text = f"Hi {username}, what would you like to do?"

    while True:
        
        choice = input("Do you want to log out or change your account's password?\n>> ").lower()

        if any(word in choice for word in logout_words):
            print("logging out")
        elif any(word in choice for word in passwd_words):
            print("changing password")
        else:
            print("invalid")


def login_sequence(accounts):
    print("\t\tWelcome back!")
    
    while True:
        user_auth = input("Enter username: ")
        passc_auth = int(input("Enter 4-digit passcode: "))
    
        if user_auth in accounts and accounts[user_auth] == passc_auth:
            print("Login successful")
            window(user_auth, accounts)
        else:
            print("username or password are incorrect")
    return user_auth


ask_input = input("Do you currently have a account with us? ")
while True:
    if ask_input in ("y", "yes"):
        login_sequence(accounts)
        break
    elif ask_input in ("n", "no"):
        #sign up sequince
        print("AAAAAAAA")
    else:
        print("Invalid response")