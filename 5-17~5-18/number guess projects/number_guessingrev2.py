#This review of the number guessing game will use functions
#and with that, I will make a main menu screen

import time
import random

def main_menu():
    while True:
        print("\t\t_____NUMBER GUESS_____\n")
        time.sleep(1)
        print("[1] Play\t[2]Quit")
        
        choice = int(input("type in either number to proceed (or not)"))
        if choice == 1:
            starting_game()
        elif choice == 2:
            print("Goodbye")
            time.sleep(2)
            break
        else:
            print("invalid option")

def starting_game():
    tries = 0
    number = random.randint(1, 10)
    
    running = True
    
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}")
    while running:
        guess = int(input("Guess the number: "))
        if guess > number:
            print("Guess is too high!")
            tries += +1
        elif guess < number:
            print("Guess is too low!")
            tries += 1
        else:
            print(F"YOU WIN! {player_name}")
            tries += 1
            print(f"\t\t######PLAYER STAT#####\t\t\n {player_name}'s guessese: {tries}")
            time.sleep(3)
            break
main_menu()

