import sys,os
sys.path.append(os.getcwd())

from app import app
import os 
import unittest
import sklearn

class AppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def tryOut(self):
        print("you have done it")
        pass
    
    def test_check(self):
        response = self.app.get('/math/check')
        self.assertEqual(response.data, b'Congratulations! Your app works. :)')

if __name__ == '__main__':
    unittest.main()
