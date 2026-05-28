import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path

#Sitka--
path = Path(__file__).parent / 'Sitka.csv'
lines = path.read_text().splitlines()          
reader = csv.DictReader(lines)
sitka_dates, sitka_highs, sitka_lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')  
    sitka_dates.append(current_date)
    sitka_highs.append(float(row['TMAX']))
    sitka_lows.append(float(row['TMIN']))

#Death valley
path = Path(__file__).parent / 'rainfall.csv'
lines = path.read_text().splitlines()
reader = csv.DictReader(lines)

dv_dates, dv_highs, dv_lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
    dv_dates.append(current_date)
    dv_highs.append(float(row['TMAX']))
    dv_lows.append(float(row['PRCP']))

plt.style.use('seaborn-v0_8')
fig, (ax1, ax2) = plt.subplots(2,1, sharey = True)

ax1.plot(sitka_dates, sitka_highs, color= 'red', alpha = 0.5)
ax1.plot(sitka_dates, sitka_lows, color = 'blue', alpha = 0.5)
ax1.fill_between(sitka_dates, sitka_highs, sitka_lows, alpha = 0.5, color= 'green')
ax1.set_title("Sitka, AK 2021", fontsize=14)
ax1.set_ylabel("Temperature (F)", fontsize=12)     

ax2.plot(dv_dates, dv_highs, color= 'red', alpha = 0.5)
ax2.plot(dv_dates, dv_lows, color = 'blue', alpha = 0.5)  
ax2.fill_between(dv_dates, dv_highs, dv_lows, alpha = 0.9, color = 'green')  
ax2.set_title("Death Valley, CA 2021", fontsize = 14)
ax2.set_ylabel("Temperature(F)", fontsize=12)

fig.suptitle("Temperature Comparison - Same Scale", fontsize=16)
fig.autofmt_xdate()
plt.savefig('16-2-comparison.png')
plt.show()