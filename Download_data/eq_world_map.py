import json
import os
from pathlib import Path
import folium

# Read the data file
input_path = Path(__file__).parent / 'eq_1_day_m1.geojson'
contents = input_path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

# Create map
eq_map = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB positron')

# Add circles
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    if mag is not None and mag > 0:
        color = 'red' if mag >= 4 else 'orange' if mag >= 2 else 'yellow'
        folium.CircleMarker(
            location=[lat, lon],
            radius=mag * 3,
            popup=f"{title} | Mag: {mag}",
            color=color,
            fill=True,
            fill_opacity=0.7,
        ).add_to(eq_map)

# Save and auto open in default browser
output = Path(__file__).parent / 'eq_map.html'
eq_map.save(str(output))

# ✅ Opens in default browser automatically
os.startfile(str(output))

print("Done!")