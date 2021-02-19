import unittest, sys
sys.path.append('..')
from makevalidparentheses import Solution

class TestMakeValidParentheses(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_min_remove_to_make_valid(self):
        case_one = 'lee(t(c)o)de)'
        self.assertEqual(self.s.minRemoveToMakeValid(case_one), 'lee(t(c)o)de')
        
        case_two = 'a)b(c)d'
        self.assertEqual(self.s.minRemoveToMakeValid(case_two), 'ab(c)d')
        
        case_three = '))(('
        self.assertEqual(self.s.minRemoveToMakeValid(case_three), '')
        
        case_four = '(a(b(c)d)'
        self.assertEqual(self.s.minRemoveToMakeValid(case_four), 'a(b(c)d)')
        
        case_five = '()'
        self.assertEqual(self.s.minRemoveToMakeValid(case_five), '()')
        
        case_six = '())()((('
        self.assertEqual(self.s.minRemoveToMakeValid(case_six), '()()')
        
if __name__ == '__main__':
    unittest.main()
