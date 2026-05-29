import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path

path = Path(__file__).parent / 'sanfran.csv'
lines = path.read_text().splitlines()
reader = csv.DictReader(lines)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
    dates.append(current_date)
    highs.append(float(row['TMAX']))
    lows.append(float(row['TMIN']))

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()                        
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, alpha = 0.999, color = 'pink')

ax.set_title("Daily High-Low Temperature - San Francisco 2021", fontsize = 16)
ax.set_xlabel('', fontsize =12)
ax.set_ylabel("Temperature (F)", fontsize = 12)

fig.autofmt_xdate()                              

plt.savefig('16_3_san_francisco.png')
plt.show()