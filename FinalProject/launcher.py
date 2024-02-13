#!/usr/bin/env python3
"""For use on linux machines"""

"""This is a final project for TLG. 
    It is a game launcher that will pick from 2 games saved in its diretory"""


#Number Picker Game
def numberpicker():
    #import section for number picker
    import random
    play = ""
    score = 0
    while play != "yes":
        print("Welcome to Number Picker! Please select your difficulty!")
        difficulty = int(input("1 easiest, 10 hardest: "))
        play = input(f"You picked {difficulty}. Ready to play? (yes/no)")

        randomness = difficulty * 10
        x = random.randrange(1, randomness)

        tries = difficulty
        if tries <= 3:
            tries = 3

        print("Let's go!")
        print(x)
        while tries > 0:
            guess = int(input(f"Pick a number between 1 and {randomness}: "))

            if guess == x :
                print("You got it! Congrats!")
                tries = 0
                score = score + (1*difficulty)
            elif guess > x:
                print("You were to high")
                tries = tries - 1
                print(f"you have {tries} guesses left.")
            elif guess < x:
                print("You were to low")
                tries = tries - 1
                print(f"you have {tries} guesses left.")

        print(f"Current score is {score}")


numberpicker()

#Trivia Game
#def trivia():

#trivia()


#Main section

#def main():






#main()