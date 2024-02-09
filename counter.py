#!/usr/bin/env python3

#Need time for pausing code
import time

#Main function will count from 0 to 10 and then break out.
def main():
    counter = 0
    while True:

        if counter < 11 :
            print(counter)
            counter = counter + 1
            time.sleep(1)
        else: 
            break
main()