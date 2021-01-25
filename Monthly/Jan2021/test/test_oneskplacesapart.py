import unittest, sys
sys.path.append('..')
from oneskplacesapart import Solution

class TestOnesKPlacesApart(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_k_length_apart(self):
        case_one = {'nums': [1,0,0,0,1,0,0,1],
                    'k': 2}
        self.assertTrue(self.s.kLengthApart(**case_one))
        
        case_two = {'nums': [1,0,0,1,0,1],
                    'k': 2}
        self.assertFalse(self.s.kLengthApart(**case_two))
        
        case_three = {'nums': [1,1,1,1,1],
                      'k': 0}
        self.assertTrue(self.s.kLengthApart(**case_three))
        
        case_four = {'nums': [0,1,0,1],
                     'k': 1}
        self.assertTrue(self.s.kLengthApart(**case_four))
        
if __name__ == '__main__':
    unittest.main()
