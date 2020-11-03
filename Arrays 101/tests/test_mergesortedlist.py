import unittest, sys
sys.path.append('..')
from mergesortedlist import Solution

class TestMergeSortedList(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_merge(self):
        case_one = {'nums1': [1,2,3,0,0,0], 'm': 3,
                    'nums2': [2,5,6], 'n': 3}
        
        self.s.merge(**case_one)
        self.assertEqual(case_one['nums1'], [1,2,2,3,5,6])
        
        
        case_two = {'nums1': [4,5,6,0,0,0], 'm': 3,
                    'nums2': [1,2,3], 'n': 3}
        
        self.s.merge(**case_two)
        self.assertEqual(case_two['nums1'], [1,2,3,4,5,6])
        
if __name__ == '__main__':
    unittest.main()
