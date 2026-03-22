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