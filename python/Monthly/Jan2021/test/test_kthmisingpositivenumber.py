import unittest, sys
sys.path.append('..')
from kthmissingpositivenumber import Solution

class TestKthMissingPositiveNumber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_kth_positive(self):
        
        # Missing number between list range
        case_one = {'arr': [2,3,4,7,11],
                    'k': 5}
        self.assertEqual(self.s.findKthPositive(**case_one), 9)
        
        # Missing number before list range start
        case_two = {'arr': [4,5,6],
                    'k': 3}
        self.assertEqual(self.s.findKthPositive(**case_two), 3)
        
        # Missing number after list range end
        case_three = {'arr': [1,2,3],
                      'k':  5}
        self.assertEqual(self.s.findKthPositive(**case_three), 8)
        
if __name__ == '__main__':
    unittest.main()
