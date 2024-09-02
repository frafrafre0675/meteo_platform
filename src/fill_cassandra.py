from cassandra.cluster import Cluster
import json

# Connexion à Cassandra
cluster = Cluster(['cassandra'])  # Utilisez 'cassandra' si vous utilisez Docker Compose
session = cluster.connect()

# Créer le keyspace si ce n'est pas déjà fait
session.execute("""
CREATE KEYSPACE IF NOT EXISTS locations
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")

# Utiliser le keyspace créé
session.set_keyspace('locations')

# Créer la table si elle n'existe pas
session.execute("""
CREATE TABLE IF NOT EXISTS places (
    id int PRIMARY KEY,
    name text,
    state text,
    country text,
    longitude double,
    latitude double
)
""")

# Charger les données JSON
with open('city.list.json', 'r') as file:
    data = json.load(file)

# Insérer les données dans la table Cassandra
for location in data:
    session.execute("""
    INSERT INTO places (id, name, state, country, longitude, latitude)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (location['id'], location['name'], location['state'], location['country'], location['coord']['lon'], location['coord']['lat']))

print("Données insérées avec succès.")
