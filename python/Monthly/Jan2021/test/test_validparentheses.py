import unittest, sys
sys.path.append('..')
from validparentheses import Solution

class TestValidParentheses(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_is_valid(self):
        case_one = '()'
        self.assertTrue(self.s.isValid(case_one))
        
        case_two = '()[]{}'
        self.assertTrue(self.s.isValid(case_two))
        
        case_three = '(]'
        self.assertFalse(self.s.isValid(case_three))
        
        case_four = '([)]'
        self.assertFalse(self.s.isValid(case_four))
        
        case_five = '{[]}'
        self.assertTrue(self.s.isValid(case_five))
        
if __name__ == '__main__':
    unittest.main()
