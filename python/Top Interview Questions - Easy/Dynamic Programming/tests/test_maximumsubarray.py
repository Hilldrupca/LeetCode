import unittest, sys
sys.path.append('..')
from maximumsubarray import Solution

class TestMaximumSubArray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_maximum(self):
        case_one = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(self.s.maxSubArray(case_one), 6)
        
        case_two = [1]
        self.assertEqual(self.s.maxSubArray(case_two), 1)
        
        case_three = [-1]
        self.assertEqual(self.s.maxSubArray(case_three), -1)
        
        case_four = [0]
        self.assertEqual(self.s.maxSubArray(case_four), 0)
        
        case_five = []
        self.assertEqual(self.s.maxSubArray(case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
