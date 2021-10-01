import json
import os
import geopandas as gdp
from glob import glob

if not os.path.exists('zones'):
    os.makedirs('zones')

# extract the created zones from the main file from energymap-contrib
# write them out to seperate files
with open('zones.geojson', 'r') as stream:
    for line in stream:
        data = json.loads(line)
        with open(f'zones/{data["properties"]["zoneName"]}.geojson', 'w') as wstream:
            wstream.write(line)

# many zones are build from smaller parts. the original repo merges this in final build step
# but that loses other info we need
# so we do this ourselves with disolve from geopandas
# execute this on each zone. if its not needed the same geojson will come back
for zone_file in glob('zones/*.geojson'):
    df = gdp.readfile(zone_file)
    df = df.dissolve()
    df.to_file(zone_file)
