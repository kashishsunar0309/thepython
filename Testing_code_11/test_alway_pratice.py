# that create in seperate file name.
'''
def get_formated_name(first,last):
    full_name = f"{first} {last}"
    return full_name.title()
#You should put name of from file name.
from alway_pratice import get_formated_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\n Please give me a first name: ")
    if first == 'q':
        break
    last = input('Please enter the last name: ')
    if last == "q":
        break
    formatted_name = get_formated_name(first,last)
    print(f"\t Nearly formatted name: {formatted_name}.")
'''
#A failing Test
'''
def get_formated_name(first,middle,last):
    "Generate a neatly formatted full name."
    full_name = f"{first}{middle}{last}"
    return full_name.title()
'''
#Resoponding to a failed test
"""
def get_formated_name(first,last,middle = ''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
"""
    
