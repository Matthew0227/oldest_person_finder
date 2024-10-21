persons_info = []

# function for name
def input_name(ask_user_for_name):
    #loop 1: asked the user for a name and ensures that the users inputs a letters only value
    while True:
        name = input(ask_user_for_name)
        if any(char.isdigit() for char in name):
            print("Please enter a name containing letters and special characters only: ")
        else:
            return name

# function for number
def input_age(ask_user_for_number):
    #loop 2: asked the user for a number and ensures that the users inputs a letters only value
    while True:
        age = input(ask_user_for_number)
        if age.isdigit():
            age = int(age)
            if 0 < age <= 120:
                return age
            else:
                print("Please enter a number between 1-120 for your age: ")
        else:
            print("Please enter a number between 1-120 for your age: ")

# function that specify the sort by age
def my_func(e):
    return e["age"]

# Loop 1: ask the user to enter value
while True:

    name = input_name("Please enter a name: ")
    age = input_age("Please enter an age: ")

    persons_info.append({"name": name, "age": age})

    try_again = input("enter another one? (y/n): ")
    try_again = try_again.lower()
    
    if try_again == "n":
        break

#sorts the persons list by age
persons_info.sort(key=my_func, reverse=True)

oldest_person = persons_info[0]


print(f"The oldest is {oldest_person['name']} who is {oldest_person['age']} years old.")
        