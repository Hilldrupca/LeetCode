import unittest, sys
sys.path.append('..')
from histogramlargestrectangle import Solution

class TestHistogramLargestRectangle(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_largest_rectangle_area(self):
        case_one = [2,1,5,6,2,3]
        self.assertEqual(self.s.largestRectangleArea(case_one), 10)
        
        case_two = [2,1,2]
        self.assertEqual(self.s.largestRectangleArea(case_two), 3)
        
        case_three = [0,1,0]
        self.assertEqual(self.s.largestRectangleArea(case_three), 1)
        
        case_four = [2,4]
        self.assertEqual(self.s.largestRectangleArea(case_four), 4)
        
        case_five = [5,4,1,2]
        self.assertEqual(self.s.largestRectangleArea(case_five), 8)
        
        case_six = [4,2,0,3,2,5]
        self.assertEqual(self.s.largestRectangleArea(case_six), 6)
        
        case_seven = list(range(20000))
        self.assertEqual(self.s.largestRectangleArea(case_seven), 100000000)
        
if __name__ == '__main__':
    unittest.main()
