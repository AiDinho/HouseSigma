import unittest
import requests
import json
import time

class TestApiUsingRequests(unittest.TestCase):
    def test_timestamp(self):
        response = requests.get('http://localhost/timestamp')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue('timestamp' in data)
        self.assertTrue(abs(data['timestamp'] - int(time.time())) < 5)

    def test_readdata(self):
        test_data = {'username': 'abc', 'password': 'xyz'}
        response = requests.post('http://localhost/readdata', json=test_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data, test_data)

    def test_noexist(self):
        response = requests.get('http://localhost/noexist')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
