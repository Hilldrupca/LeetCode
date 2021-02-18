import unittest, sys
sys.path.append('..')
from checkdoubleexists import Solution

class TestCheckDoubleExists(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_check_if_exists(self):
        case_one = [10,2,5,3]
        self.assertTrue(self.s.checkIfExists(case_one))
        
        case_two = [7,1,14,11]
        self.assertTrue(self.s.checkIfExists(case_two))
        
        case_three = [3,1,7,11]
        self.assertFalse(self.s.checkIfExists(case_three))
        
        case_four = [-2,0,10,-19,4,6,-8]
        self.assertFalse(self.s.checkIfExists(case_four))
        
        case_five = []
        self.assertFalse(self.s.checkIfExists(case_five))
        
if __name__ == '__main__':
    unittest.main()
