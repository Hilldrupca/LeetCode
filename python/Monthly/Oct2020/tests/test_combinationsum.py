import unittest, sys
sys.path.append('..')
from combinationsum import Solution

class TestCombinationSum(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_combination_sum(self):
        case_one = {'candidates': [2,3,6,7],
                    'target': 7}
        
        ans_one = self.s.combinationSum(**case_one)
        self.assertIn([2,2,3], ans_one)
        self.assertIn([7], ans_one)
        
        
        case_two = {'candidates': [2,3,5],
                    'target': 8}
        
        ans_two = self.s.combinationSum(**case_two)
        self.assertIn([2,3,3], ans_two)
        self.assertIn([2,2,2,2], ans_two)
        self.assertIn([3,5], ans_two)
        
        
        case_three = {'candidates': [2],
                      'target': 1}
        
        ans_three = self.s.combinationSum(**case_three)
        self.assertEqual(ans_three, [])
        
        
        case_four = {'candidates': [1],
                     'target': 2}
        
        ans_four = self.s.combinationSum(**case_four)
        self.assertEqual(ans_four, [[1,1]])
        
if __name__ == '__main__':
    unittest.main()
