import unittest, sys
sys.path.append('..')
from carpooling import Solution

class TestCarPooling(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_carPooling(self):
        case_one = {'trips': [[2,1,5],[3,3,7]],
                    'capacity': 4}
        self.assertFalse(self.s.carPooling(**case_one))
        
        case_two = {'trips': [[2,1,5],[3,3,7]],
                    'capacity': 5}
        self.assertTrue(self.s.carPooling(**case_two))
        
        case_three = {'trips': [[2,1,5],[3,5,7]],
                      'capacity': 3}
        self.assertTrue(self.s.carPooling(**case_three))
        
        case_four = {'trips': [[3,2,7],[3,7,9],[8,3,9]],
                     'capacity': 11}
        self.assertTrue(self.s.carPooling(**case_four))
        
if __name__ == '__main__':
    unittest.main()
