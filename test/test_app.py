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

    def test_add(self):
        '''Positive scenario of adding given list of numbers'''
        response = self.app.post('/math/add', json={'numbers':[1, 2, 3, 4]})
        self.assertEqual(response.data, b'10', 'Addition is not correct')

    def test_add_empty(self):
        '''to verify addition of emty data'''
        response = self.app.post('/math/add', json={})
        self.assertEqual(response.data, b'0', 'Addition is not correct')

    def test_add_floats(self):
        '''to verify addition of float numbers'''
        response = self.app.post('/math/add', json={'numbers':[1, 2.3, 4.5]})
        self.assertEqual(response.data, b'7.8', 'Addition is not correct')

    def test_add_negative(self):
        '''to verify addition of negative numbers'''
        response = self.app.post('/math/add', json={'numbers':[1, -1, 2, -3]})
        self.assertEqual(response.data, b'-1', 'Addition is not correct')

if __name__ == '__main__':
    unittest.main()