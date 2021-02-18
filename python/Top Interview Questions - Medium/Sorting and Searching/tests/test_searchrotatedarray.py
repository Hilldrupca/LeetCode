import unittest, sys
sys.path.append('..')
from searchrotatedarray import Solution

class TestSearchRotatedArray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_search(self):
        case_one = {'nums': [4,5,6,7,0,1,2],
                    'target': 0}
        self.assertEqual(self.s.search(**case_one), 4)
        
        
        case_two = {'nums': [4,5,6,7,0,1,2],
                    'target': 3}
        self.assertEqual(self.s.search(**case_two), -1)
        
        
        case_three = {'nums': [5,1,3],
                      'target': 3}
        self.assertEqual(self.s.search(**case_three), 2)
        
        
        case_four = {'nums': [1],
                     'target': 0}
        self.assertEqual(self.s.search(**case_four), -1)
        
if __name__ == '__main__':
    unittest.main()
