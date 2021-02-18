import unittest, sys
sys.path.append('..')
from smallestrangeII import Solution

class TestSmallestRangeII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_smallest_range_II(self):
        case_one = {'A': [1],
                    'K': 0}
        self.assertEqual(self.s.smallestRangeII(**case_one), 0)
        
        case_two = {'A': [0,10],
                    'K': 2}
        self.assertEqual(self.s.smallestRangeII(**case_two), 6)
        
        case_three = {'A': [1,3,6],
                      'K': 3}
        self.assertEqual(self.s.smallestRangeII(**case_three), 3)
        
if __name__ == '__main__':
    unittest.main()
