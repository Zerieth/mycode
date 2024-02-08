#!/usr/bin/env python3
"""Understanding Dictionaries 
    {key: value, key: value, ...} """

def main():
    #Runtime function

    ##create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip":"10.0.1.1", "version":"1.2", "vendor":"cisco"}

    ##displays dictionary
    print(switch)

    print(type(switch))

    ##display parts of the dictionary
    print( switch["hostname"] ) #should display sw1
    print( switch["ip"] ) #should display "10.0.1.1"

    #This next bit will break the program
    print( "First use of get() method")
    print( switch.get("lynx")) #this will return none

    #This will customize what is returned if key isn't found
    print( "Second Test of get method")
    print( switch.get("lynx", "The key is invalid") )

    print( "Third test of get")
    print( switch.get("version")) #this should work

if __name__ == "__main__":
    main()