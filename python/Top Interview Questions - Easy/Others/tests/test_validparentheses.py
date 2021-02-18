import unittest, sys
sys.path.append('..')
from validparentheses import Solution

class TestValidParentheses(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_is_valid(self):
        self.assertTrue(self.s.isValid('()'))
        self.assertTrue(self.s.isValid('()[]{}'))
        self.assertTrue(self.s.isValid('{[]}'))
        
        self.assertFalse(self.s.isValid('(]'))
        self.assertFalse(self.s.isValid('([)]'))
        
if __name__ == '__main__':
    unittest.main()
