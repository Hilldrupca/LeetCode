import unittest, sys
sys.path.append('..')
from searchrotatedarrayII import Solution

class TestSearchRotatedArrayII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_search(self):
        case_one = {'nums': [2,5,6,0,0,1,2],
                    'target': 0}
        self.assertTrue(self.s.search(**case_one))
        
        case_two = {'nums': [2,5,6,0,0,1,2],
                    'target': 3}
        self.assertFalse(self.s.search(**case_two))
        
        case_three = {'nums': [4,5,6,7,0,1,2],
                      'target': 0}
        self.assertTrue(self.s.search(**case_three))
        
        case_four = {'nums': [1,3,1,1,1],
                     'target': 3}
        self.assertTrue(self.s.search(**case_four))
        
        case_five = {'nums': [1,1,3,1],
                     'target': 3}
        self.assertTrue(self.s.search(**case_five))
        
        case_six = {'nums': [1],
                    'target': 0}
        self.assertFalse(self.s.search(**case_six))
        
if __name__ == '__main__':
    unittest.main()
