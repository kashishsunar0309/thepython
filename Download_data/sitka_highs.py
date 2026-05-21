from pathlib import Path
import csv

# Step 1: Open the CSV file
path = Path('Download_data/detail.csv')
lines = path.read_text().splitlines()

# Step 2: Read the CSV content
reader = csv.reader(lines)

# Step 3: Get the first row (header row)
header_row = next(reader)

# Step 4: Print each column name with its position number
for index, column_header in enumerate(header_row):
    print(index, column_header)