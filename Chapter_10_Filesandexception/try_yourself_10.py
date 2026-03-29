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
