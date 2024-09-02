import unittest
from consumer import consume_weather_data

class TestConsumer(unittest.TestCase):

    def test_consume_weather_data(self):
        data = consume_weather_data()
        self.assertIsNotNone(data)
        self.assertIn('city', data)
        self.assertIn('temperature', data)

if __name__ == "__main__":
    unittest.main()