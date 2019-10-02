import sys,os,random,functools,json
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

        # Multiplication Test
        test_data = {
            'data':{}
        }
        
        ints = [random.randint(0,50) for i in range(15)]
        for i in range(len(ints)):
            test_data['data']['param'+str(i)] = ints[i]
        
        mul_test = json.loads(self.app.post('/math/product',json = json.dumps(test_data)).data)
        self.assertEqual(mul_test['result'],functools.reduce(lambda x,y: x*y,ints))

        # Division test
        test_data['data'] = {
            'param1': random.randint(1,50),
            'param2': random.randint(1,50)
        }
        div_test = json.loads(self.app.post('/math/division',json = json.dumps(test_data)).data)
        self.assertEqual(div_test['result'], test_data['data']['param1']/test_data['data']['param2'])

        # Addition test
        test_data['data'] = {}
        for i in range(len(ints)):
            test_data['data']['param'+str(i)] = ints[i]
        add_test = json.loads(self.app.post('/math/add',json = json.dumps(test_data)).data)
        self.assertEqual(add_test['result'], sum(ints))

if __name__ == '__main__':
    unittest.main()