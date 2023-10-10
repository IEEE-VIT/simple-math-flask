import sys
import os
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

    def test_addition(self):
        data = {"num1": 3, "num2": 4}
        response = self.app.post('/math/add', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": 7})

    def test_multiplication(self):
        data = {"num1": 2, "num2": 5}
        response = self.app.post('/math/multiply', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": 10})

if __name__ == '__main__':
    unittest.main()
