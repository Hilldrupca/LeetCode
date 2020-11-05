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
        
        case_three = [1]
        self.assertFalse(self.s.validMountainArray(case_three))
        
        case_four = [0,3,2,1]
        self.assertTrue(self.s.validMountainArray(case_four))
        
if __name__ == '__main__':
    unittest.main()
