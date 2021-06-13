import json
import os

if not os.path.exists('zones'):
    os.makedirs('zones')

with open('zones.geojson', 'r') as stream:
    for line in stream:
        data = json.loads(line)
        with open(f'zones/{data["properties"]["zoneName"]}.geojson', 'w') as wstream:
            wstream.write(line)
