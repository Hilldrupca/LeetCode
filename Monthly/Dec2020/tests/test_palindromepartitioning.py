import unittest, sys
sys.path.append('..')
from palindromepartitioning import Solution

class TestPalindromePartitioning(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_partition(self):
        ans_one = self.s.partition('aab')
        exp_ans = [['a','a','b'],['aa','b']]
        
        self.assertEqual(len(ans_one), len(exp_ans))
        for ans in exp_ans:
            self.assertIn(ans, ans_one)
            
        ans_two = self.s.partition('a')
        exp_ans = [['a']]
        
        self.assertEqual(len(ans_two), len(exp_ans))
        for ans in exp_ans:
            self.assertIn(ans, ans_two)
            
        ans_three = self.s.partition('racecar')
        exp_ans = [['racecar'],
                   ['r','aceca','r'],
                   ['r','a','cec','a','r'],
                   ['r','a','c','e','c','a','r']]
        
        self.assertEqual(len(ans_three), len(exp_ans))
        for ans in exp_ans:
            self.assertIn(ans, ans_three)
            
            
        self.assertEqual(self.s.partition(''),[])
if __name__ == '__main__':
    unittest.main()
