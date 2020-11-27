import unittest, sys
sys.path.append('..')
from equalsubsetsum import Solution

class TestEqualSubsetSum(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_can_partition(self):
        case_one = [1,5,11,5]
        self.assertTrue(self.s.canPartition(case_one))
        
        case_two = [3,3,3,4,5]
        self.assertTrue(self.s.canPartition(case_two))
        
        case_three = [1,2,3,5]
        self.assertFalse(self.s.canPartition(case_three))
        
        case_four = [1,2,5]
        self.assertFalse(self.s.canPartition(case_four))
        
        case_five = []
        self.assertFalse(self.s.canPartition(case_five))
        
if __name__ == '__main__':
    unittest.main()
