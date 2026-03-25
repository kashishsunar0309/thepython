from pathlib import Path
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
print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("\n Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number)/ int(second_number)
    print(answer)