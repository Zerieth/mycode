#!/usr/bin/env python3

# Defining round outside of the program


def main():

    round = 0

    while True:
        round = round + 1
        # The question!

        print('Finish the movie title, "Monty Python\'s The Life of _____"')

        # The answer field. Adjusts for user input

        answer = input("Your guess---> ")
        answer = answer.capitalize()

        # If statements to check the users answer. Will loop up to 3 times
        if answer == 'Brian':
            print('Correct')
            break
        elif round == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Incorrect. Try again!")

main()
