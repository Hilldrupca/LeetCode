import unittest, sys
sys.path.append('..')
from countlis import Solution

class TestCountLis(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_number_of_lis(self):
        case_one = [1,3,5,4,7]
        self.assertEqual(self.s.findNumberOfLIS(case_one), 2)
        
        case_two = [1,3,5,4,7,6,8]
        self.assertEqual(self.s.findNumberOfLIS(case_two), 4)
        
        case_three = [2,2,2,2,2]
        self.assertEqual(self.s.findNumberOfLIS(case_three), 5)
        
        case_four = [5,6,7,1,2,3,4,10]
        self.assertEqual(self.s.findNumberOfLIS(case_four), 1)
        
        case_five = []
        self.assertEqual(self.s.findNumberOfLIS(case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
