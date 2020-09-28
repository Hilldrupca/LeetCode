import unittest, sys
sys.path.append('..')
from subarrayproductlessthank import Solution

class TestSubarrayProductLessThanK(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().numSubarrayProductLessThanK
        
    def test_num_subarray_product_less_than_k(self):
        case_one = {'nums': [10,5,2,6],
                    'k': 100}
        self.assertEqual(self.s(**case_one), 8)
        
        case_two = {'nums': [1,1,1],
                    'k': 1}
        self.assertEqual(self.s(**case_two), 0)
        
        case_three = {'nums': [2,3,4],
                      'k': 0}
        self.assertEqual(self.s(**case_three), 0)
        
if __name__ == '__main__':
    unittest.main()
