import unittest, sys
sys.path.append('..')
from validmountainarray import Solution

class TestValidMountainArray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_valid_mountain_array(self):
        case_one = [2,1]
        self.assertFalse(self.s.validMountainArray(case_one))
        
        case_two = [3,5,5]
        self.assertFalse(self.s.validMountainArray(case_two))
        
        case_three = [0,3,2,1]
        self.assertTrue(self.s.validMountainArray(case_three))
        
        case_four = [0,1,2,3,4,5,6,7,8,9]
        self.assertFalse(self.s.validMountainArray(case_four))
        
        case_five = [9,8,7,6,5,4,3,2,1,0]
        self.assertFalse(self.s.validMountainArray(case_five))
        
if __name__ == '__main__':
    unittest.main()
