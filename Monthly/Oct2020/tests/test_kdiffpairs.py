import unittest, sys
sys.path.append('..')
from kdiffpairs import Solution

class TestKDiffPairs(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_pairs(self):
        case_one = {'nums': [3,1,4,1,5],
                    'k': 2}
        self.assertEqual(self.s.findPairs(**case_one), 2)
        
        
        case_two = {'nums': [1,2,3,4,5],
                    'k': 1}
        self.assertEqual(self.s.findPairs(**case_two), 4)
        
        
        case_three = {'nums': [1,3,1,5,4],
                      'k': 0}
        self.assertEqual(self.s.findPairs(**case_three), 1)
        
        
        case_four = {'nums': [1,2,4,4,3,3,0,9,2,3],
                     'k': 3}
        self.assertEqual(self.s.findPairs(**case_four), 2)
        
        
        case_five = {'nums': [-1,-2,-3],
                     'k': 1}
        self.assertEqual(self.s.findPairs(**case_five), 2)
        
if __name__ == '__main__':
    unittest.main()
