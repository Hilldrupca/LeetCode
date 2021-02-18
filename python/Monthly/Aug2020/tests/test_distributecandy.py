import unittest, sys
sys.path.append('..')
from distributecandy import Solution

class TestDistributeCandy(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        self.assertEqual(self.s.distributeCandies(7,4), [1, 2, 3, 1])
        self.assertEqual(self.s.distributeCandies(10,3), [5, 2, 3])
        
if __name__ == '__main__':
    unittest.main()
