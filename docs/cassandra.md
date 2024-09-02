# Acces cassandra

docker exec -it cassandra cqlsh

## Création d'un Keyspace & d'une Table

CREATE KEYSPACE IF NOT EXISTS Locations WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE Locations;

CREATE TABLE IF NOT EXISTS places (
    id int PRIMARY KEY,
    name text,
    state text,
    country text,
    longitude double,
    latitude double
);

### Script Python pour Charger et Insérer les Données

from cassandra.cluster import Cluster
import json

cluster = Cluster(['cassandra'])
session = cluster.connect('locations')

with open('../meteo_platform/data/city.list.json', 'r') as file:
    locations = json.load(file)

for location in locations:
    query = """
    INSERT INTO places (id, name, state, country, longitude, latitude)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    session.execute(query, (location['id'], location['name'], location['state'], location['country'], location['coord']['lon'], location['coord']['lat']))

print("Données insérées avec succès.")

#### Tester

SELECT * FROM places;
