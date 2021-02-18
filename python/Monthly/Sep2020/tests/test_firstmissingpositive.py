import unittest, sys
sys.path.append('..')
from firstmissingpositive import Solution

class TestFirstMissingPositive(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_first_missing_positive(self):
        self.assertEqual(self.s.firstMissingPositive([1,2,0]), 3)
        self.assertEqual(self.s.firstMissingPositive([3,4,-1,1]), 2)
        self.assertEqual(self.s.firstMissingPositive([7,8,9]), 1)
        self.assertEqual(self.s.firstMissingPositive([0,2,2,1,1]), 3)
        
if __name__ == '__main__':
    unittest.main()
