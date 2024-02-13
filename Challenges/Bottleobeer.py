#!/usr/bin/env python3

import time

def main():
    
    #Gathers input from user
    x = int(input("How many bottles should I count?: "))
    
    #Checks to ensure input is within bounds
    if (1 <= x <= 100):
    #else:
        #print ("Not within bounds")
        #time.sleep(2)
        #x = int(input(" How many bottles should I count?: "))

        while x >= 1:
            print(f"{x} bottles of beer on the wall, {x} bottles of beer.")
            x = x - 1
            print(f"Take one down, pass it around, {x} bottles of beer on the wall")
        

main()


    
