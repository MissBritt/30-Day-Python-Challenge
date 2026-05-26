# Bank account program
# Base done #5/25/26

import random
import time
passcode = 4321
balance = 100


# BANK INTERFACE
def bank_interface():
    global balance
    welcome_msg = f"\t-------------Welcome {username}-------------\t"
  
    for i in range(10):
        print(".")
   
    while True:
        for i in range(20):
            print(".")

        main_ui = f"\t| Current Balance: {balance} |\t\n\n\t[1]DEPOSIT\t[2]WITHDRAW"
       
        print(welcome_msg.upper())
        print(main_ui)
       
        ui_nav = int(input("\nSelect Option>> "))
        if ui_nav == 1:
            deposit_input = int(input("How much would you like to deposit? >> $"))
            if deposit_input > 0:
                balance += deposit_input
                print("Balance added successfully!")
                time.sleep(2)
        elif ui_nav == 2:
            deposit_input = int(input("How much would you like to withdraw? >> $"))
            if deposit_input > 0:
                balance -= deposit_input
                print("Balance Withdrawn successfully!")
                time.sleep(2)
        else:
            print("Not a valid choice, please try again")
    
#THE ARE YOU SURE? FUNCTION (I don't know if I am actually gonna put this in lol)
"""def ask_again():
    ask_input = int(input("Are you sure you want to select this option?\n[1]Yes\t[2]Cancel\nSelect Option>> "))
    while True:
        if ask_input == 1:
            break
        elif ask_input == 2:
            bank_interface()
        else:
            print("Not a valid choice, please try again")"""


#LAUNCH ANIMATION/INITIATION
for i in range(4):
    time.sleep(1)
    print(".", end="", flush=True)

print("\nWelcome to The Bank of Brittannica")
username = input("Please enter name...\n\n")
print(f"Welcome {username}")
time.sleep(1)

while True:
    pass_input = int(input("\nPlease enter four digit passcode...\n\n"))
    if pass_input == passcode:
        print("access granted")
        for i in range(3):
            print(".", flush=True )
        time.sleep(1)
        bank_interface()
        break   
    else:
        print("the passcode you entered was incorrect or not valid")
