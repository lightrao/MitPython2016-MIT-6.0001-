import unittest
from blackBoxTesting import sqrt

class TestSquareRoot(unittest.TestCase):
    def test_sqrt(self):
        # Test square root
        self.assertAlmostEqual(sqrt(0,0.0001)**2,0,delta=0.0001)
        self.assertAlmostEqual(sqrt(25,0.0001)**2,25,delta=0.0001)
        self.assertAlmostEqual(sqrt(0.05,0.0001)**2,0.05,delta=0.0001)
        self.assertAlmostEqual(sqrt(2,0.0001)**2,2,delta=0.0001)
        # self.assertAlmostEqual(sqrt(2,0.5**64)**2,2,delta=0.5**64)
        