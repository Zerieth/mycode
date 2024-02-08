#!/usr/bin/env python3


def main():


    while True:
#Below is a list of marvel characters in dictionary format

        marvelchars= {
            "Starlord":
            {"real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"},

            "Mystique":
            {"real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"},

            "Hulk":
            {"real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"} 
                          }

    
        # Ask which character user wants to know about

        input_name = input( "Which character do you want to know about? (Starlord, Mystique, Hulk): " )
        input_name = input_name.capitalize()
        # Ask which stat they want to learn

        input_attr = input(" What statistic do you want to know about? (real name, powers, archenemy): ")
        input_attr = input_attr.lower()
        # a print function with this output <char_name>'s <char_stat> is: <value>
        #If statement will check to apply the title method to only real name call backs

        if input_attr == "real name":
            print(f"{input_name}'s {input_attr} is:  {marvelchars[input_name][input_attr].title()}" )
        else:
            print(f"{input_name}'s {input_attr} is:  {marvelchars[input_name][input_attr]}" )

            #line will determine if user is finished

        input_continue = input("Are you finished? Type exit to close: ")
        

        if input_continue.lower() == "exit":
            break

main()
