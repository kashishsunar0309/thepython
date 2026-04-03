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
'''#Assertion Programm
#before run this program you should create a file name alway_pratice
#inside alway_practice file created function get_formated_name
from alway_pratice import get_formated_name
def test_first_last_name():
    formatted_name = get_formated_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'''
    
