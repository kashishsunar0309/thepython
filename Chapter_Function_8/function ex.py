# Exercise
# Defining Function
def greet_user(username):
    print(f"Hello, {username.title()}")
greet_user('kashish')

# Passing arguments
# Positional argument
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(pet_name='hamster', animal_type='harry')  # keyword arguments

# Default values
def describe_pet_1(animal_type, pet_name='willie'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet_1(animal_type='cat')

# Passing arguments
# Positional argument
def describe_pet_2(animal_type2, pet_name2):
    print(f"\nI have a {animal_type2}.")
    print(f"My {animal_type2}'s name is {pet_name2.title()}.")
describe_pet_2('hamster', 'harry')
describe_pet_2('dog', 'willie')
describe_pet_2(pet_name2='hamster', animal_type2='harry')  # keyword arguments

# Default values
def describe_pet_1a(animal_type1a, pet_name1a='willie'):
    print(f"\nI have a {animal_type1a}.")
    print(f"My {animal_type1a}'s name is {pet_name1a.title()}.")
describe_pet_1a(animal_type1a='cat')

# Return values example
def multiply(a, b):
    return a * b
product = multiply(4, 6)
print(product)

# Return values example
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making argument optional
def get_formatted_name1(first_name1, last_name1, middle_name1=''):
    full_name1 = f"{first_name1} {middle_name1} {last_name1}"
    return full_name1.title()
musician1 = get_formatted_name1('john', 'lee', 'hooker')
print(musician1)

# For choice two or three
def get_formatted_name2(first_name2, middle_name2, last_name2):
    if middle_name2:
        full_name2 = f"{first_name2} {middle_name2} {last_name2}"
    else:
        full_name2 = f"{first_name2} {last_name2}"
    return full_name2.title()
musician2 = get_formatted_name2('jimi', 'hendrix', "")
print(musician2)
musician3 = get_formatted_name2('john', 'hooker', 'lee')
print(musician3)

# Returning a Dictionary
def build_person(first_name3, last_name3):
    person = {'first': first_name3, 'last': last_name3}
    return person
musician4 = build_person('jimi', 'hendrix')
print(musician4)

# Using a function with a while loop
# This is an infinite loop
def get_formatted_name3(first_name4, last_name4):
    full_name3 = f"{first_name4} {last_name4}"
    return full_name3.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name3(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# With quit option
def get_formatted_name4(first_name5, last_name5):
    full_name4 = f"{first_name5} {last_name5}"
    return full_name4.title()

while True:
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")
    f_name1 = input("First name: ")
    if f_name1 == 'q':
        break
    l_name1 = input("Last name: ")
    if l_name1 == 'q':
        break
    formatted_name1 = get_formatted_name4(f_name1, l_name1)
    print(f"\nHello, {formatted_name1}!")