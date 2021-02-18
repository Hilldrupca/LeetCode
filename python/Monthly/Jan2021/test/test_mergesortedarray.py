import unittest, sys
sys.path.append('..')
from mergesortedarray import Solution

class TestMergeSortedArray(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_merge(self):
        
        # Both lists populated
        case_one = {'nums1': [1,2,3,0,0,0],
                    'm': 3,
                    'nums2': [2,5,6],
                    'n': 3}
        self.s.merge(**case_one)
        self.assertEqual(case_one['nums1'], [1,2,2,3,5,6])
        
        # Only nums1 populated
        case_two = {'nums1': [1],
                    'm': 1,
                    'nums2': [],
                    'n': 0}
        self.s.merge(**case_two)
        self.assertEqual(case_two['nums1'], [1])
        
        # Only nums2 populated
        case_three = {'nums1': [0],
                      'm': 0,
                      'nums2': [1],
                      'n': 1}
        self.s.merge(**case_three)
        self.assertEqual(case_three['nums1'], [1])
        
if __name__ == '__main__':
    unittest.main()
