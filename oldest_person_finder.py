# Create a program that ask user to input name and age. 
# Print error message when the input is not valid. 
# Set your own definition of valid name and valid age. 
# Store all the collected information into array. 
# After every input, ask the user if want to input another entry. 
# When “Yes”, ask the user again for input. Do it until the user respond “No”. 
# When the user responded “No”, display the name and age of the oldest person.  
# Use the array in checking who is the oldest

# variables
persons_list = {}
new_person_info = {}

# function for name
def input_name(ask_user_for_name):
    while True:
        name = input(ask_user_for_name)
        if name.isalpha():
            return name
        else:
            print("Please enter a name containing letters only: ")

# function for number
def input_age(ask_user_for_number):
    while True:
        age = input(ask_user_for_number)
        if age.isdigit():
            age = int(age)
            if 0 < age <= 120:
                print("rerer")
                return age
        else:
            print("Please enter a number between 1-120 for your age: ")

name = input_name("Please enter a name: ")
age = input_age("Please enter an age: ")


# Loop 1: ask the user to enter value
while True:
    new_person_info[age] = {
        "name" : name,
        "age" : age
    }

    try_again = input("enter another one? (y/n): ")
    try_again = try_again.lower()
    
    if try_again == "n":
            # ends the loop 1 if the user enters the letter n
        print(new_person_info)
        break

        