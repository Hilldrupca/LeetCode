import unittest, sys
sys.path.append('..')
from climbingstairs import Solution

class TestClimbingStairs(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_climb(self):
        self.assertEqual(self.s.climbStairs(2), 2)
        
        self.assertEqual(self.s.climbStairs(5), 8)
        
        self.assertEqual(self.s.climbStairs(8), 34)
        
        self.assertEqual(self.s.climbStairs(20), 10946)
        
if __name__ == '__main__':
    unittest.main()
