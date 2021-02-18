import unittest, sys
sys.path.append('..')
from squaresofsortedarray import Solution

class TestSquaresOfSortedArray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_sorted_squares(self):
        case_one = [-4,-1,0,3,10]
        self.assertEqual(self.s.sortedSquares(case_one), [0,1,9,16,100])
        
        case_two = [-7,-3,2,3,11]
        self.assertEqual(self.s.sortedSquares(case_two), [4,9,9,49,121])
        
if __name__ == '__main__':
    unittest.main()
