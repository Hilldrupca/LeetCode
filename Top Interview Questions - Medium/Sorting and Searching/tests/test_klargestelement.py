import unittest, sys
sys.path.append('..')
from klargestelement import Solution

class TestKLargestElement(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_kth_largest(self):
        case_one = {'nums': [3,2,1,5,6,4],
                    'k': 2}
        self.assertEqual(self.s.findKthLargest(**case_one), 5)
        
        
        case_two = {'nums': [3,2,3,1,2,4,5,5,6],
                    'k': 4}
        self.assertEqual(self.s.findKthLargest(**case_two), 4)
        
if __name__ == '__main__':
    unittest.main()
