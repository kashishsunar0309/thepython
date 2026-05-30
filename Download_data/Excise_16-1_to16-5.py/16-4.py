import csv
from datetime import datetime
import matplotlib.pyplot as plt 
from pathlib import Path
path = Path(__file__).parent / 'Sitka.csv'
lines = path.read_text().splitlines()
reader = csv.DictReader(lines)

#Get indexes automatically from header.
header = reader.fieldnames
tmax_index = header.index('TMAX')
tmin_index = header.index('TMIN')
name_index = header.index('NAME')

dates, highs, lows = [], [], []
station_name = ''
for row in reader:
    current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
    dates.append(current_date)
    highs.append(float(row['TMAX']))
    lows.append(float(row['TMIN']))
    if not station_name:
        station_name = row['NAME']
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, alpha = 0.88, color = 'purple')

ax.set_title(f"Daily High_Low Temperatures - {station_name} 2021", fontsize = 14)
ax.set_ylabel("Temperature (F)", fontsize = 12)

plt.savefig('16_4_auto_index.png')
plt.show()