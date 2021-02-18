import unittest, sys
sys.path.append('..')
from smallestdivisorthreshold import Solution

class TestSmallestDivisorThreshold(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_smallest_divisor(self):
        case_one = {'nums': [1,2,5,9],
                    'threshold': 6}
        self.assertEqual(self.s.smallestDivisor(**case_one), 5)
        
        case_two = {'nums': [2,3,5,7,11],
                    'threshold': 11}
        self.assertEqual(self.s.smallestDivisor(**case_two), 3)
        
        case_three = {'nums': [19],
                      'threshold': 5}
        self.assertEqual(self.s.smallestDivisor(**case_three), 4)
        
        case_four = {'nums': [22,22,22,22],
                     'threshold': 4}
        self.assertEqual(self.s.smallestDivisor(**case_four), 22)
        
if __name__ == '__main__':
    unittest.main()
