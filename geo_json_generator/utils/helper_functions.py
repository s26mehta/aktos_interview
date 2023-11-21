import csv
import json
import os

from .class_definitions import *
from geo_json_generator.models import ConsumerData

def csv_import(url):
    url_open = urllib.request.urlopen(url)
    csvfile = csv.reader(io.TextIOWrapper(url_open.read().decode('utf-8')), delimiter=',') 
    return csvfile;


def process_csv_data(csv_file = 'consumers.csv'):
    new_rows = []

    # Empty ConsumerData
    ConsumerData.objects.all().delete()
    
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, csv_file)
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            new_row = ConsumerData(
                id = row['id'],
                street = row['street'],
                status = row['status'],
                previous_jobs_count = int(row['previous_jobs_count']),
                amount_due = row['amount_due'],
                lat = row['lat'],
                long = row['lng']
            )
            new_rows.append(new_row)
    
    ConsumerData.objects.bulk_create(new_rows)


def get_consumers(min_previous_jobs_count, max_previous_jobs_count, status):
    if status != None:
        data = ConsumerData.objects.filter(previous_jobs_count__gte=min_previous_jobs_count,previous_jobs_count__lte=max_previous_jobs_count, status=status)
    else:
        data = ConsumerData.objects.filter(previous_jobs_count__gte=min_previous_jobs_count,previous_jobs_count__lte=max_previous_jobs_count)

    features = []
    for row in data:
        features.append(
            Feature(
                geometry = Point(
                    coordinates = [float(row.lat), float(row.long)]
                ),
                properties = Properties(
                    id = row.id,
                    amount_due = float(row.amount_due),
                    previous_jobs_count = row.previous_jobs_count,
                    status = row.status,
                    street = row.street
                )
            )
        )
    
    geo_json = GeoJson(features)
    return json.dumps(geo_json, cls=JsonConverter)