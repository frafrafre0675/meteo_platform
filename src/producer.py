import json
import requests
from kafka import KafkaProducer

API_KEY = "f8545d4dcefd85b1a2225882e3d79cf5"
KAFKA_TOPIC = "weather_data"
KAFKA_SERVER = "localhost:9092"

def get_weather_data(city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def main():
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    with open('data/city.list.json') as f:
        cities = json.load(f)
    
    for city in cities:
        data = get_weather_data(city['id'])
        producer.send(KAFKA_TOPIC, data)
        print(f"Sent weather data for {city['name']} to Kafka")

if __name__ == "__main__":
    main()
