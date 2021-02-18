import unittest, sys
sys.path.append('..')
from arithmeticslices import Solution

class TestArithmeticSlices(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_number_of_arithmetic_slices(self):
        case_one = [1,2,3,4]
        self.assertEqual(self.s.numberOfArithmeticSlices(case_one), 3)
        
        case_two = [1,3,5,7,9]
        self.assertEqual(self.s.numberOfArithmeticSlices(case_two), 6)
        
        case_three = [7,7,7,7]
        self.assertEqual(self.s.numberOfArithmeticSlices(case_three), 3)
        
        case_four = [3,-1,-5,-9]
        self.assertEqual(self.s.numberOfArithmeticSlices(case_four), 3)
        
        case_five = [1,1,2,5,7]
        self.assertEqual(self.s.numberOfArithmeticSlices(case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
