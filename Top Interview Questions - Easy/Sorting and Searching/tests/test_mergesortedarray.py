import unittest, sys
sys.path.append('..')
from mergesortedarray import Solution

class TestMergeSortedArray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_merge(self):
        nums1 = [1,2,3,0,0,0]
        case_one = {'nums1': nums1,
                    'm': 3,
                    'nums2': [2,5,6],
                    'n': 3}
        self.s.merge(**case_one)
        self.assertEqual(nums1, [1,2,2,3,5,6])
        
if __name__ == '__main__':
    unittest.main()
