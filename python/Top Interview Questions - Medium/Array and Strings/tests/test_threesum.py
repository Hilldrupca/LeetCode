import unittest, sys
sys.path.append('..')
from threesum import Solution

class TestThreeSum(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_three_sum(self):
        case_one = [-1,0,1,2,-1,-4]
        answer_one = self.s.threeSum(case_one)
        self.assertIn((-1,-1,2), answer_one)
        self.assertIn((-1,0,1), answer_one)
        
        # Test for list with fewer than three elements
        self.assertEqual(self.s.threeSum([]), [])
        self.assertEqual(self.s.threeSum([0]), [])
        self.assertEqual(self.s.threeSum([-1,-1]), [])
        
if __name__ == '__main__':
    unittest.main()
