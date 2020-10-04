import unittest, sys
sys.path.append('..')
from coveredintervals import Solution

class TestCoveredIntervals(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().removeCoveredIntervals
        
    def test_remove_covered_intervals(self):
        case_one = [[1,4],
                    [3,6],
                    [2,8]]
        self.assertEqual(self.s(case_one), 2)
        self.assertIn([1,4], case_one)
        self.assertIn([2,8], case_one)
        self.assertNotIn([3,6], case_one)
        
        
        case_two = [[1,4],
                    [2,3]]
        self.assertEqual(self.s(case_two), 1)
        self.assertIn([1,4], case_two)
        self.assertNotIn([2,3], case_two)
        
        
        case_three = [[0,10],
                      [5,12]]
        self.assertEqual(self.s(case_three), 2)
        self.assertIn([0,10], case_three)
        self.assertIn([5,12], case_three)
        
        
        case_four = [[3,10],
                     [4,10],
                     [5,11]]
        self.assertEqual(self.s(case_four), 2)
        self.assertIn([3,10], case_four)
        self.assertIn([5,11], case_four)
        self.assertNotIn([4,10], case_four)
        
        
        case_five = [[1,2],
                     [1,4],
                     [3,4]]
        self.assertEqual(self.s(case_five), 1)
        self.assertIn([1,4], case_five)
        self.assertNotIn([1,2], case_five)
        self.assertNotIn([3,4], case_five)
        
if __name__ == '__main__':
    unittest.main()
