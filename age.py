#!/usr/bin/python3
#This script will collect and return a users age. It will also inform if the entered age is invalid


#This line welcomes the user 
print("Welcome to the age input form, were you tell me your age and I repeat it back to you!")

#This line will collect a valid int input

while True:
    try:
        age = int(input("Tell me your age: "))
    except ValueError:
        print("This is not a number")
        continue
    else:
        break



#This determines if the age is valid range
if 0 <= age <= 110:
    print("You are", age, "years old")
else:
    print("Invalid age")
exit()

