import sys,os
sys.path.append(os.getcwd())

from app import app
import os 
import unittest

class AppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_check(self):
        response = self.app.get('/math/check')
        self.assertEqual(response.data, b'Congratulations! Your app works. :)')

    def test_multiply(self):
        response = self.app.post('/math/multiply', json={"input": [1,2,3,4,5]})
        self.assertEqual(response.json["output"], 120)

    def test_multiply_with_no_data(self):
        response = self.app.post('/math/multiply')
        self.assertEqual(response.json["error"], "Input expected")
    
    def test_multiply_with_invalid_input(self):
        response = self.app.post('/math/multiply', json={"input": 1})
        self.assertEqual(response.json["error"], "Invalid input, expected an iterable")

if __name__ == '__main__':
    unittest.main()