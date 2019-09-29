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

    def test_sum(self):
        response = self.app.post('/math/add', data={'numbers': '2,3,5,1'})
        self.assertEqual(response.data, b'Sum of [2, 3, 5, 1] = 11')

if __name__ == '__main__':
    unittest.main()