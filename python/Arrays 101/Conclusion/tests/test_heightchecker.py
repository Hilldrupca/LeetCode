import unittest, sys
sys.path.append('..')
from heightchecker import Solution

class TestHeightChecker:
    
    def setUp(self):
        self.s = Solution()
        
    def test_height_checker(self):
        case_one = [1,1,4,2,1,3]
        self.assertEqual(self.s.heightChecker(case_one), 3)
        
        case_two = [5,1,2,3,4]
        self.assertEqual(self.s.heightChecker(case_two), 5)
        
        case_three = [1,2,3,4,5]
        self.assertEqual(self.s.heightChecker(case_three), 0)
        
if __name__ == '__main__':
    unittest.main()
