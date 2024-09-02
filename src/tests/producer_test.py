import unittest
from producer import produce_weather_data

class TestProducer(unittest.TestCase):

    def test_produce_weather_data(self):
        data = produce_weather_data()
        self.assertIsNotNone(data)
        self.assertIn('city', data)
        self.assertIn('temperature', data)

if __name__ == "__main__":
    unittest.main()
