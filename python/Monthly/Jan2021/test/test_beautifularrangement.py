import unittest, sys
sys.path.append('..')
from beautifularrangement import Solution

class TestBeautifulArrangment(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_count_arrangement(self):
        cases = list(range(1, 16))
        exp_answers = [1,
                       2,
                       3,
                       8,
                       10,
                       36,
                       41,
                       132,
                       250,
                       700,
                       750,
                       4010,
                       4237,
                       10680,
                       24679]
        
        for case, ans in zip(cases, exp_answers):
            with self.subTest(case=case, answer=ans):
                self.assertEqual(self.s.countArrangement(case), ans)
                
if __name__ == '__main__':
    unittest.main()
