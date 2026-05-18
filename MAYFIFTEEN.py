import time
import random

done = False
#Welcome Prompt
while not done:
    
    guess = 0
    guesses = 0
    number = random.randint(1, 10)
    player_name = input("Welcome to the guessing game, what is your name?")
    time.sleep(1)
    print(f"Hi, {player_name}!")
    time.sleep(1)

    #Game
    while True:
        guess = int(input("Guess the number! "))
        if guess > number:
            print("Too High")
            guesses += 1
        elif guess < number:
            print("Too low")
            guesses += 1
        else:
            time.sleep(1)
            print("You win!")
            break

    #Stats
    print(f"\t\t######PLAYER STAT#####\t\t\n {player_name}'s guessese: {guesses}")

    play_again = input("Would you like to play again? [TYPE Y or N] ")
    if play_again.lower() == 'n':
       print("game end")
       done = True
