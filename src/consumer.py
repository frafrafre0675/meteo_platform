from kafka import KafkaConsumer
from cassandra.cluster import Cluster
import json

KAFKA_TOPIC = "weather_data"
KAFKA_SERVER = "localhost:9092"

def main():
    consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('weather_keyspace')

    for message in consumer:
        data = message.value
        session.execute("""
            INSERT INTO weather_data (city_id, city_name, timestamp, temperature, humidity, weather_description)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (data['id'], data['name'], data['dt'], data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']))
        print(f"Inserted data for {data['name']} into Cassandra")

if __name__ == "__main__":
    main()
