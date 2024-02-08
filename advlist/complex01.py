#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - using the extend method"""

def main():

    #creates list of 3 different animals and prints it
    animals = ["Fox", "Eagle", "Tiger"]

    print(animals)

    #collects user input to add 2 new items

    exanimals = input("Add a new animal")
    exanimals1 = input("add one more!")

    #extends original animals value and prints new result
    animals.append(exanimals)
    animals.append(exanimals1)
    print(animals)
main()

