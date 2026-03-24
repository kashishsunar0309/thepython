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