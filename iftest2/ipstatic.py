#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true

if ipchk == "192.168.70.1":
    print("This is a default gateway. " + ipchk + "is not recommended for use.")
elif  "192.168.70.2" <= ipchk <= "192.168.70.254":
   print("Looks like the IP address was set: " + ipchk) # indented under if
else:     #data not provided
    print("You did not provide a valid input")