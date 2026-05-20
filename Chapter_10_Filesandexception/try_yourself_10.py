#10-1
"""
from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text()
print("---Reading the entire file: ---")
print(contents)
print()
#10-2
#from pathlib import Path
path = Path ('learning_python.txt')
contents = path.read_text()
print("--- Replacing Python with C: ---")
for line in contents.splitlines():
    modified_line = line.replace('python','c')
    print(modified_line)
print()
#10-3
#from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text()
for line in contents.splitlines():
    print(line.replace('Python','C'))
"""
"""
#10-4
from pathlib import Path
name = input("What's is your name: ")
path = Path('guest.txt')#To saw the world you should create file name
#guest.txt then what give name in terminal that automatic print in guest.txt file
path.write_text(name)"""
"""
#10-5
from pathlib import Path
print("Type 'quit', to stop.\n")
contents = ""
while True:
    name = input('enter the name:')
    if name.lower() == "quit":
        break
    contents += name + '\n'
path = Path("guest_boook.txt")#where program work to see create file name
#guest_book.txt where what enter the terminal that will print in guest_book.txt file
path.write_text(contents)   
"""
'''#10-6 tryyourself
print("Enter two number, and I'll add them together.")
try:
    x_str = input("First number: ")
    x = int(x_str)
    y_str = input("Second number: ")
    y = int(y_str)
except ValueError:
    print("Sorry , I really need a number to do math! Please try again.")
else:
    sum = x + y
    print(f"The sum of (x) and (y) is {sum}.")
# 10-7 try yourself
print("-- welcome to the Addition Calculator ----")
print("Enter 'q' any time to quit.\n" )
while True:
    #1 Get the first input
    first_number = input("First number: ")
    if first_number.lower() == 'q':
        break
    #Get the second input
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break
    #Use tryexcept to handle potential text input errors
    try:
        #We try to convert and add in one go
        result = int(first_number)+int(second_number)
    except ValueError:
        #This triggers if int() fails
        print("Error, I can only add numbers. Please try again. ")
    else:
        #This only runs if no ValueError occurred
        print(f"The Total is : {result}")
    print("-"*20)
print("Goodbye!")'''
#10-8:
"""
from pathlib import Path
filenames = ["cats.txt","dogs.txt"]
for filename in filenames:
    path = Path(filename)
    print(f"\n Reading file: {filename}")
    try:
        contents = path.read_text()
    except FileNotFoundError:
        #This cathes the errors if you moved or deleted the file.
        print(f"Error : The file '{filename}' was not found.")
    else:
        print(contents)
#10-9:
try:
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
    #'pass' tells python. "I know there's an error, just keep going."
    pass
"""
#10-10
"""
from pathlib import Path
def count_words(filename,word):
    '''Count the approximate number of times a word appears in a file'''
    path = Path(filename)
    try:
        contents = path.read_text(encoding = "utf-8")
    except FileNotFoundError:
        print(f"Sorry , the file {filename} doesn't exit")
    else:
        #count 'the' (include words like 'then','there','them')
        word_count = contents.lower().count(word)
        #Count 'the' with a space (more likely to be just the word 'the')
        strict_count = contents.lower().count(f"{word}")
        print(f"File : {filename}")
        print(f"Searching for '{word}':(with space): {strict_count} matches.")
files = ['cats.txt','dogs.txt']
for file in files:
    count_words(file,'the')
    """
#For run this program you should file like file_name.json.
#for json.dump file
"""from pathlib import Path
import json
numbers = [2,5,6,7,8,9,56,45,34,23,78]
path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
"""
#for json.upload file
"""
from pathlib import Path
import json
path = Path('numbers.json')
contents = path.read_text()
number = json.loads(contents)
print(number)
"""
#Saving and reading User-Generated Data
"""
from pathlib import Path
import json
username = input("What's your name? ")
path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back,{username}")
#for json.upload 
from pathlib import Path
import json
path = Path("username.json")
contents = path.read_text()
username = json.loads(contents)
print(f"Welcome back, {username}")
"""
#10-11
'''
from pathlib import Path
import json
fav_num = int(input("Enter the number: "))
path = Path('fav_num.json')
contents = json.dumps(fav_num)
path.write_text(contents)
print(f"I know your favorite number it's {fav_num} ?")
#10-12
path = Path('fav_num.json')
contents = path.read_text()
numbers = json.loads(contents)
print(fav_num)
'''
#10-13
'''
from pathlib import Path
import json
path = Path('user_info.json')
if path.exists():
    user = json.loads(path.read_text())
else:
    user = {}
    user['username'] = input("What's is your name: ")
    user['city'] = input("What city are you from ?")
    user['language'] = input("What's your favorite programming language?")
    path.write_text(json.dumps(user))
print(" \n Here's what I remember about you:")
print(f" Username: {user['username']}")
print(f"City: {user['city']}")
print(f"Favorite language: {user['language']}")
'''
#10-14
'''
from pathlib import Path
import json
def get_stored_username(path):
    if path.exists():
        return json.loads(path.read_text())
    return None
def get_new_username(path):
    username = input("What's your name?: ")
    path.write_text(json.dumps(username))
    return username
def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        confirm = input(f"Are you {username}?(yes/no): ")
        if confirm.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back,{username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
greet_user()'''    