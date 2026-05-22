from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Step 1: Open the CSV file
path = Path(__file__).parent / 'detail.csv'
lines = path.read_text().splitlines()

# Step 2: Read the CSV content
reader = csv.reader(lines)

# Step 3: Get the first row (header row)
header_row = next(reader)

# Extracting high temperature
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Format plot
ax.set_title("Daily High Temperature, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

print(highs)
plt.show()