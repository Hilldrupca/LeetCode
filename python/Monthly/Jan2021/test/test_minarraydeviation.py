import unittest, sys
sys.path.append('..')
from minarraydeviation import Solution

class TestMinArrayDeviation(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_minimum_deviation(self):
        case_one = [1,2,3,4]
        self.assertEqual(self.s.minimumDeviation(case_one), 1)
        
        case_two = [4,1,5,20,3]
        self.assertEqual(self.s.minimumDeviation(case_two), 3)
        
        case_three = [2,10,8]
        self.assertEqual(self.s.minimumDeviation(case_three), 3)
        
        case_four = [3,5]
        self.assertEqual(self.s.minimumDeviation(case_four), 1)
        
        case_five = [10,4,8]
        self.assertEqual(self.s.minimumDeviation(case_five), 1)
        
        case_six = [10,4,3]
        self.assertEqual(self.s.minimumDeviation(case_six), 2)
        
if __name__ == '__main__':
    unittest.main()
