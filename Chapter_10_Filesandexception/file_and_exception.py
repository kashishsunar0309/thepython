"""from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
birthday = input("Enter the your brithday, in the from mmddy: ")
if birthday in pi_string:
    print("Your birth appears in the first million digits of pi ! ")
else:
    print('Your birthday doesnot appear in the first million digits of pi.')
#second execise of file and exception.
"""
"""from pathlib import Path
contents = "I love programming.\n"
contents += 'I love creating new games.\n'
contents += 'I also love working with data.\n'
path = Path('programing.txt')
#writing single file
#path.write_text("I love Math and progamming with connection between there.")
#writing multi line file
path.write_text(contents)
"""
#print(5\0) Don't run so, using try-except blocks
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")
"""
"""
print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("\n Second number: ")
    if second_number == 'q':
        break
    #THE ELSE BL0CK
    try :
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0! ")
    else:
        print(answer)'''
#Handling the FileNOtFoundError Exception
from pathlib import Path
path = Path('alice.txt')
try:
  contents = path.read_text(encoding = "uft - 8")
except FileNotFoundError:
  print(f"Sorry, the file  {path} doesn't exist.")
#ANALYZING TEXT
#(https://gutenberg.org) for Project Gutenberg for work with literary text. IMPORTANT FOR BELOW ELSE CODE.
from pathlib import Path
path = Path('alice.txt')
try:
 contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
 print(f"Sorry, the file {path} does not exist.")
else:
 # Count the approximate number of words in the file:
  words = contents.split()
  num_words = len(words)
  print(f"The file {path} has about {num_words} words.")
"""
#multiple files
"""
from pathlib import Path
def count_words(filename):
#Count the appreciate number of words in a file
    try:
        contents = filename.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist ")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The  file {filename} has about {num_words} words.")
# analyze of multiple file
filenames = ['alice.txt','moby.txt','siddhartha.txt','kashish.txt']
#before we run this program you should file with nameoffile.txt
for filename in filenames:
    path = Path(filename)
    count_words(path)
#Falling silently

from pathlib import Path
def count_words(filename):
#Count the appreciate number of words in a file
    try:
        contents = filename.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The  file {filename} has about {num_words} words.")
filenames = ['alice.txt','moby.txt','siddhartha.txt','kashish.txt']
#before we run this program you should file with nameoffile.txt
for filename in filenames:
    path = Path(filename)
    count_words(path)
    """