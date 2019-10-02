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

    def test_power_without_data(self):
        response = self.app.post('/math/power')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], "Input expected!")
    
    def test_power_without_base_value(self):
        response = self.app.post('/math/power', json={"exponent": 1})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], "Base value expected!")
    
    def test_power_without_exponent_value(self):
        response = self.app.post('/math/power', json={"base": 2})
        self.assertEqual(response.json["result"], 1)

    def test_power_success(self):
        response  = self.app.post('/math/power', json={"base": 2, "exponent": 3})
        self.assertEqual(response.json["result"], 8)

if __name__ == '__main__':
    unittest.main()