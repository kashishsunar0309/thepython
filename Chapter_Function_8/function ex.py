#Execise
#Defininig Function
def greet_user(username):
    print(f"Hello,{username.title()}")
greet_user('kashish')
"""
#passing arguments
    #positional argument
"""
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet(pet_name ='hamster',animal_type ='harry') # keyword arguments

#default values
def describe_pet_1(animal_type,pet_name='willie'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet_1(animal_type = 'cat')