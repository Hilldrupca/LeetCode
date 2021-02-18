import unittest, sys
sys.path.append('..')
from inctripletsub import Solution

class TestIncTripletSub(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_increasing_triplet(self):
        case_one = [1,2,3,4,5]
        self.assertTrue(self.s.increasingTriplet(case_one))
        
        case_two = [5,4,3,2,1]
        self.assertFalse(self.s.increasingTriplet(case_two))
        
        case_three = [2,1,5,0,4,6]
        self.assertTrue(self.s.increasingTriplet(case_three))
        
        case_four = [1,1,1]
        self.assertFalse(self.s.increasingTriplet(case_four))
        
        case_five = [3,2]
        self.assertFalse(self.s.increasingTriplet(case_five))
        
        case_six = []
        self.assertFalse(self.s.increasingTriplet(case_six))
        
if __name__ == '__main__':
    unittest.main()
