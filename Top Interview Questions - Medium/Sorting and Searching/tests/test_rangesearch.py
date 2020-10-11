import unittest, sys
sys.path.append('..')
from rangesearch import Solution

class TestRangeSearch(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_search_range(self):
        case_one = {'nums': [5,7,7,8,8,10],
                    'target': 8}
        self.assertEqual(self.s.searchRange(**case_one), [3,4])
        
        
        case_two = {'nums': [5,7,7,8,8,10],
                    'target': 6}
        self.assertEqual(self.s.searchRange(**case_two), [-1,-1])
        
        
        case_three = {'nums': [],
                      'target': 0}
        self.assertEqual(self.s.searchRange(**case_three), [-1,-1])
        
        
        case_four = {'nums': [3,3,3],
                     'target': 3}
        self.assertEqual(self.s.searchRange(**case_four), [0,2])
        
if __name__ == '__main__':
    unittest.main()
