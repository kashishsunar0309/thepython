import urllib.request
from pathlib import Path

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson'
output = Path(__file__).parent / 'eq_1_day_m1.geojson'

urllib.request.urlretrieve(url, output)
print("Downloaded successfully!")