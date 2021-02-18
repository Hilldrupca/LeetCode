import unittest, sys
sys.path.append('..')
from longestharmonioussubsequence import Solution

class TestLongestHarmoniousSubsequence(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_LHS(self):
        case_one = [1,3,2,2,5,2,3,7]
        self.assertEqual(self.s.findLHS(case_one), 5)
        
        case_two = [1,2,3,4]
        self.assertEqual(self.s.findLHS(case_two), 2)
        
        case_three = [1,1,1,1]
        self.assertEqual(self.s.findLHS(case_three), 0)
        
        case_four = [1,2,2,1]
        self.assertEqual(self.s.findLHS(case_four), 4)
        
        case_five = [1,2,2,3,4,5,1,1,1,1]
        self.assertEqual(self.s.findLHS(case_five), 7)
        
        case_six = [-3,-1,-1,-1,-3,-2]
        self.assertEqual(self.s.findLHS(case_six), 4)
        
if __name__ == '__main__':
    unittest.main()
