import json
import csv
import os

with open('world-json.json', encoding='utf8') as f:
    data = json.load(f)

if not os.path.exists('csv-files'):
    os.makedirs('csv-files')

for feature in data['features']:
    file_name = feature.get('properties').get('ADMIN')
    coords = feature.get('geometry').get('coordinates')[0][0]

    with open(f'csv-files/{file_name}.csv', 'w', newline='') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',')

        data_writer.writerow(['Latitude', 'Longitude'])

        for coord in coords:
            data_writer.writerow(coord)