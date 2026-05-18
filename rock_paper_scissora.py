#Brushing up on basics by making rock, paper, sciossors game
#Features menu and scoretracking
import time
import random

def player_name():
    name =input("Enter name: ")
    print(f"Welcome {name}")
    print("\tStarting...")
    time.sleep(1)
    return name

def start_game(name, wins):
    computer_choice_list = ['rock', 'paper', 'scissors']
    wins = 0
    while True:
        computer_choice = random.choice(computer_choice_list)
        player_choice = input("Choose wisely...\nRock\nPaper\nScissors\nEnhter choice: ")
        if player_choice == computer_choice:
            print(f"You chose {player_choice}")
            time.sleep(1)
            print(f"Computer chose {computer_choice}")
            print("TIE!")
            time.sleep(1)
        elif player_choice == "rock" and computer_choice == "scissors":
            print(f"You chose {player_choice}")
            time.sleep(1)
            print(f"Computer chose {computer_choice}")
            print(f"{name} wins!")
            wins += 1
            play_again(name, wins)
            break
        elif player_choice == "paper" and computer_choice == "rock":
            print(f"You chose {player_choice}")
            time.sleep(1)
            print(f"Computer chose {computer_choice}")
            wins += 1
            print("Player wins!")
            play_again(name, wins)
            break
        elif player_choice == "scissors" and computer_choice == "paper":
            print(f"You chose {player_choice}")
            time.sleep(1)
            print(f"Computer chose {computer_choice}")
            wins += 1
            print("Player wins!")
            play_again(name, wins)
            break
        else:
            print(f"You chose {player_choice}")
            time.sleep(1)
            print(f"Computer chose {computer_choice}")
            print("You lose :(")
            play_again(name, wins)
            break
    return wins
def play_again(name, wins):
    while True:
        time.sleep(1)
        prompt = int(input("Would you like to play again or quit to menu?\n[1]PLAY AGAIN\t[2]QUIT TO MAIN MENU"))
        if prompt == 1:
            start_game(name, wins)
            break
        elif prompt == 2:
            menu(name, wins)
        else:
            print("Pick a valid number")

def menu(name, wins):
    while True:
        menu_options = int(input("\t_____ROCK PAPER SCISSORS_____\n\n\n[1]Play\t[2]Current wins\n[3]Quit\nChoose number: "))
        if menu_options == 1:
            print("Loading...\n\n\n")
            time.sleep(2)
            wins = start_game(name, wins)
            break
        elif menu_options == 2:
            print(f"{name} has {wins} wins")
            input("press ENTER...")
        elif menu_options == 3:
            print("Goodbye")
            time.sleep(2)
            break

#MAIN FUNCTIONM -----------------------------
def main():
    name = player_name()
    wins = 0
    menu(name, wins)

main()
    