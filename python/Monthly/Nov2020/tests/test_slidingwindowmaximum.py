import unittest, sys
sys.path.append('..')
from slidingwindowmaximum import Solution

class TestSlidingWindowMaximum(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_sliding_window(self):
        case_one = {'nums': [1,3,-1,-3,5,3,6,7],
                    'k': 3}
        self.assertEqual(self.s.maxSlidingWindow(**case_one), [3,3,5,5,6,7])
        
        case_two = {'nums': [1],
                    'k': 1}
        self.assertEqual(self.s.maxSlidingWindow(**case_two), [1])
        
        case_three = {'nums': [1,-1],
                     'k': 1}
        self.assertEqual(self.s.maxSlidingWindow(**case_three), [1,-1])
        
        case_four = {'nums': [9,11],
                     'k': 2}
        self.assertEqual(self.s.maxSlidingWindow(**case_four), [11])
        
        case_five = {'nums': [4,-2],
                     'k': 2}
        self.assertEqual(self.s.maxSlidingWindow(**case_five), [4])
        
        case_six = {'nums': [5,4,3,2,1],
                    'k': 3}
        self.assertEqual(self.s.maxSlidingWindow(**case_six), [5,4,3])
        
        case_seven = {'nums': [10,9,8,7,6,5,4,3,2,1],
                      'k': 3}
        self.assertEqual(self.s.maxSlidingWindow(**case_seven),
                         [10,9,8,7,6,5,4,3])
        
        case_eight = {'nums': [],
                      'k': 3}
        self.assertEqual(self.s.maxSlidingWindow(**case_eight), [])
        
        case_nine = {'nums': [1,2,3],
                     'k': 0}
        self.assertEqual(self.s.maxSlidingWindow(**case_nine), [])
        
if __name__ == '__main__':
    unittest.main()
