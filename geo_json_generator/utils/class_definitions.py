import json

class Properties:
    def __init__(self, id, amount_due, previous_jobs_count, status, street):
        self.id = id
        self.amount_due = amount_due
        self.previous_jobs_count = previous_jobs_count
        self.status = status
        self.street = street
    
    def create_json(self):
        self.__dict__

class Point:
    def __init__(self, coordinates):
        self.type = "Point"
        self.coordinates = coordinates

    def create_json(self):
        self.__dict__

class Feature:
    def __init__(self, geometry, properties):
        self.type = "Feature"
        self.geometry = geometry
        self.properties = properties

    def create_json(self):
        self.__dict__

class GeoJson:
    def __init__(self, features):
        self.type = "FeatureCollection"
        self.features = features

    def create_json(self):
        self.__dict__

class JsonConverter(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__