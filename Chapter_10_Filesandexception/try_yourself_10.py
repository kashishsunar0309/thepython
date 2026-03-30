#10-1
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
    """"
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
