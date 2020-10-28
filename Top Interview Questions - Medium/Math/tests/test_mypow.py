import unittest, sys
sys.path.append('..')
from mypow import Solution

class TestMyPow(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_my_pow(self):
        self.assertEqual(self.s.myPow(2.00000, 10), pow(2.00000, 10))
        self.assertEqual(self.s.myPow(2.10000, 3), pow(2.10000, 3))
        self.assertEqual(self.s.myPow(2.0000, -2), pow(2.00000, -2))
        
if __name__ == '__main__':
    unittest.main()
