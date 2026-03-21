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