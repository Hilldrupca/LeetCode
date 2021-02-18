import unittest, sys
sys.path.append('..')
from mostwatercontainer import Solution

class TestMostWaterContainer(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_area(self):
        case_one = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(self.s.maxArea(case_one), 49)
        
        case_two = [1,1]
        self.assertEqual(self.s.maxArea(case_two), 1)
        
        case_three = [4,3,2,1,4]
        self.assertEqual(self.s.maxArea(case_three), 16)
        
        case_four = [1,2,1]
        self.assertEqual(self.s.maxArea(case_four), 2)
        
if __name__ == '__main__':
    unittest.main()
