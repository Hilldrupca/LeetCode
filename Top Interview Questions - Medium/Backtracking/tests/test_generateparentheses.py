import unittest, sys
sys.path.append('..')
from generateparentheses import Solution

class TestGenerateParentheses(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_generate_parentheses(self):
        ans_one = self.s.generateParentheses(3)
        expected_ans = ["((()))","(()())","(())()","()(())","()()()"]
        
        for expected in expected_ans:
            self.assertIn(expected, ans_one)
            
        self.assertEqual(len(ans_one), 5)
        
        
        ans_two = self.s.generateParentheses(2)
        expected_ans = ["(())","()()"]
        
        for expected in expected_ans:
            self.assertIn(expected, ans_two)
            
        self.assertEqual(len(ans_two), 2)
        
        
        self.assertEqual(self.s.generateParentheses(0), [])
        
if __name__ == '__main__':
    unittest.main()
