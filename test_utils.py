# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018


import unittest
from utils import *
class TestUtils(unittest.TestCase):
    def test_fact(self):
      self.assertEqual(fact(3),6)    
      self.assertEqual(fact(2),2)
      pass
    def test_roots(self):
        self.assertEqual(roots(3,3,0),('{}', '-1.0'))
        self.assertEqual(roots(2,2,2),('',''))
        pass
    
    def test_integrate(self):
        self.assertEqual(integrate(ff,0,1), 0.49998500010000024)
        self.assertEqual(integrate(gg,0,1), 0.9999700002000005)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
#test2
