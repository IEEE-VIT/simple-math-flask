import json
import sys
import os
sys.path.append(os.getcwd())

from app import app
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

    def test_logarithm_router(self):
        response = self.app.post('/math/logarithm')
        self.assertEqual(response.status_code, 200)

    def test_logarithm_with_error_cases(self):
        response = self.app.post('/math/logarithm')
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'No input was provided.')

        response = self.app.post('/math/logarithm', json={'fakeinput': 42})
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'No number to calculate a logarithm was provided.')

    def test_logarithm_with_correct_cases(self):
        response = self.app.post('/math/logarithm', json={'number': 1})
        data = json.loads(response.data)
        self.assertEqual(data['result'], 0)

        response = self.app.post('/math/logarithm', json={'number': 8, 'base': 2})
        data = json.loads(response.data)
        self.assertEqual(data['result'], 3)

if __name__ == '__main__':
    unittest.main()
