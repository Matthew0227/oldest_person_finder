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

# Loop 1: ask the user to enter value
while True:
    try:
        name = input("Please enter a name: ")
        #loop 2: requires the user to enter a name repeatedly until it enters the correct value
        while True:
            try:
                if name != name.isdigit():
                    # ends the loop 2
                    break
            except ValueError:
                print("Please enter a name containing letters only: ")

        age = input("Please enter your age: ")
        #loop 3: requires the user to enter an age repeatedly until it enters the correct value
        while True:
            try:
                if age == age.isdigit():
                    if 0 < age <= 120:
                        # ends the loop 3
                        break
            except ValueError:
                print("Please enter a number between 1-120 for your age: ")

        new_person_info[age] = {
            "name" : name,
            "age" : age
        }

        persons_list.append(new_person_info)

        try_again = input("enter another one? (y/n): ")
        try_again = try_again.lower()

        if try_again == "n":
            # ends the loop 1 if the user enters the letter n
            break
    except ValueError:
        print(persons_list[len(persons_list)])


        