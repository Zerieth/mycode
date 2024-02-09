#!/bin/usr/env python3
#Above for linux based operating systems

#Goals: Use ELIF statements to take inputs and determine outputs
#Use While to add break out to code


#This code is a pick a number game. It will tell the user if they are below or above the number

import random
import time

def main():
    play_again="None"
    print("Let's play Number Guesser!")

    while play_again.lower() != "no":
        x = 1
        answer = random.randint(1, 10)

        guess = 0

    #The game itself runs within this while statement

        while x <= 3:       #This runs for 3 rounds. Each failed guess adds to x
            guess = int(input("Pick a number between 1 and 10: "))
            if guess == answer:
                print("You guessed it right! Good job!")
                time.sleep(2)
                play_again = input("Would you like to play again?: ")
                break
            elif guess < answer:
                print("Pick higher")
                x = x + 1
                time.sleep(2)
            elif guess > answer:
                print("Pick lower!")
                x = x + 1
                time.sleep(2)
        #Statement runs when you run out of guesses.
        else:
            print("Darn you ran out of guesses.")
            time.sleep(2)
            play_again = input("Would you like to play again?: ") #Prompts player to play again



main()
