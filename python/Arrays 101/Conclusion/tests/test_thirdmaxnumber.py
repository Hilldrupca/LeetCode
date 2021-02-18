import unittest, sys
sys.path.append('..')
from thirdmaxnumber import Solution

class ThirdMaxNumber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_third_max(self):
        case_one = [3,2,1]
        self.assertEqual(self.s.thirdMax(case_one), 1)
        
        case_two = [1,2]
        self.assertEqual(self.s.thirdMax(case_two), 2)
        
        case_three = [2,2,3,1]
        self.assertEqual(self.s.thirdMax(case_three), 1)
        
        case_four = []
        self.assertEqual(self.s.thirdMax(case_four), float('-inf'))
        
if __name__ == '__main__':
    unittest.main()
