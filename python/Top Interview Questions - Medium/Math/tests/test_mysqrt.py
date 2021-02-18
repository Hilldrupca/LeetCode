import unittest, sys
sys.path.append('..')
from mysqrt import Solution

class TestMySqrt(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_my_sqrt(self):
        self.assertEqual(self.s.mySqrt(4),2)
        self.assertEqual(self.s.mySqrt(8),2)
        
if __name__ == '__main__':
    unittest.main()
