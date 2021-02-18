import unittest, sys
sys.path.append('..')
from longestincreasingsubsequence import Solution

class TestLongestIncreasingSubsequence(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_length_of_lis(self):
        case_one = [10,9,2,5,3,7,101,18]
        self.assertEqual(self.s.lengthOfLIS(case_one), 4)
        
        case_two = []
        self.assertEqual(self.s.lengthOfLIS(case_two), 0)
        
        case_three = [0]
        self.assertEqual(self.s.lengthOfLIS(case_three), 1)
        
        case_four = [10,9,2,5,3,4]
        self.assertEqual(self.s.lengthOfLIS(case_four), 3)
        
        case_five = [1,3,6,7,9,4,10,5,6]
        self.assertEqual(self.s.lengthOfLIS(case_five), 6)
        
        case_six = [2,2]
        self.assertEqual(self.s.lengthOfLIS(case_six), 1)
        
if __name__ == '__main__':
    unittest.main()
