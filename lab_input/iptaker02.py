#!/usr/bin/python3
"""Alta3 Research | RZFeeser
    print() - display data to std out"""

#below is a function containing our code
def main():
    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")

    
    
    #display the input back to the user
    # print("You told me the IPv4 address is: ", user_input)

    #This portion records the users device name and displays it back to the user
    user_device = input("Please enter the device name")
    print("The IP address and device name are")
    print(user_device)
    print(user_input)
   

#this calls the main
main()

