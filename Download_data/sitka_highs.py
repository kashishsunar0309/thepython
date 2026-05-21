from pathlib import Path
import csv

# Step 1: Open the CSV file
path = Path('detail.csv')
lines = path.read_text().splitlines()

# Step 2: Read the CSV content
reader = csv.reader(lines)

# Step 3: Get the first row (header row)
header_row = next(reader)

#Exatracting high tempature
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)
print(highs)