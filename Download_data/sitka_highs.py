from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Open the CSV file
path = Path(__file__).parent / 'detail.csv'
lines = path.read_text().splitlines()

# Step 2: Read the CSV content
reader = csv.reader(lines)

# Step 3: Get the first row (header row)
header_row = next(reader)

# Extracting high temperature
dates, highs , lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs,color = 'red')
ax.plot(highs, color='red')
ax.plot(lows, color = 'blue')

# Format plot
ax.set_title("Daily High Temperature and Low Temperature, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

print(highs)
plt.show()