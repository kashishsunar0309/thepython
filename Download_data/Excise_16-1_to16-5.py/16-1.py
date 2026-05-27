import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path

path = Path(__file__).parent / 'rainfall.csv'
lines = path.read_text().splitlines()
reader = csv.DictReader(lines)

dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
    prcp = float(row['TMAX'])  # Changed from 'PRCP' to 'TMAX'
    dates.append(current_date)
    prcps.append(prcp)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, prcps, color='blue') #Dates is not a error but that is warning for code .

ax.set_title("Daily Rainfall - Sitka, AK 2021", fontsize=16)
ax.set_xlabel('', fontsize=12)
ax.set_ylabel("Rainfall (inches)", fontsize=12)
fig.autofmt_xdate()

plt.savefig('16_1_sitka_rainfall.png')
plt.show()