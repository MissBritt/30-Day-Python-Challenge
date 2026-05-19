# Bank account program

import random
import time
passcode = 4321

# BANK INTERFACE

def bank_interface():
   for i in range(10):
    print(".")
   
   welcome_msg = f"\t-------------Welcome {username}-------------\t"
   ui_list = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
   print(ui_list)
   print(welcome_msg.upper())

#LAUNCH ANIMATION/INITIATION

for i in range(4):
    pass
    time.sleep(1)
    print(".", end="", flush=True)

print("\nWelcome to The Bank of Brittannica")
username = input("Please enter name...\n\n")
print(f"Welcome {username}")
time.sleep(1)

while True:
    pass
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
