import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path

#Sitka rainfall
path = Path(__file__).parent / 'Sitka.csv'
lines = path.read_text().splitlines()
reader = csv.DictReader(lines)

sitka_dates, sitka_rain = [], []
for row in reader:
    current_date = datetime.strptime(row['DATE'],'%Y-%m-%d')
    sitka_dates.append(current_date)
    # Bug Fix 1: Skip rows where PRCP is empty
    if row['PRCP']:
        sitka_rain.append(float(row['PRCP']))
    else:
        sitka_rain.append(0.0)

#Death Valley rainfall
path = Path(__file__).parent / 'rainfall.csv'
lines = path.read_text().splitlines()
reader = csv.DictReader(lines)

dv_dates, dv_rain = [], []
for row in reader:
    current_date = datetime.strptime(row['DATE'],'%Y-%m-%d')
    dv_dates.append(current_date)
    # Bug Fix 1 (same): Skip rows where PRCP is empty
    if row['PRCP']:
        dv_rain.append(float(row['PRCP']))
    else:
        dv_rain.append(0.0)

plt.style.use('seaborn-v0_8')
# Bug Fix 2: plt.subplot → plt.subplots (missing 's')
fig, (ax1,ax2) = plt.subplots(2, 1, sharey=True)

ax1.bar(sitka_dates, sitka_rain, color='blue')
ax1.set_title("Sitka, AK - Daily Rainfall 2021", fontsize=14)
ax1.set_ylabel("Rainfall (inches)", fontsize=12)

ax2.bar(dv_dates, dv_rain, color='orange')
ax2.set_title("Death Valley, CA - Daily Rainfall 2021", fontsize=14)
ax2.set_ylabel("Rainfall (inches)", fontsize=16)

fig.suptitle("Rainfall Comparison", fontsize=16)
fig.autofmt_xdate()
plt.savefig("16-5_explore.png")
plt.show()