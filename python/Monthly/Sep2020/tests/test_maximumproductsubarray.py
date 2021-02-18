import unittest, sys
sys.path.append('..')
from maximumproductsubarray import Solution

class TestMaximumProductSubarray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_maxProduct(self):
        cases = {6: [2,3,-2,4],
                 0: [-2,0,-1],
                 12: [-4,-3],
                 42: [-2,-3,7],
                 0: [0],
                 2: [0,2],
                 4: [3,-1,4],
                 1: [0,-3,1,1],
                 1: [-2,1,0]}
        
        for answer, nums in cases.items():
            self.assertEqual(self.s.maxProduct(nums), answer)
            
if __name__ == '__main__':
    unittest.main()
