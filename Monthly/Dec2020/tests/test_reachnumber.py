import unittest, sys
sys.path.append('..')
from reachnumber import Solution

class TestReachNumber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_reach_number(self):
        cases = [1,
                 2,
                 5,
                 47,
                 50,
                 53,
                 100,
                 678,
                 1000,
                 9987,
                 1000000000]
        
        answers = [1,
                   3,
                   5,
                   10,
                   11,
                   10,
                   15,
                   39,
                   47,
                   141,
                   44723]
        
        for case, ans in zip(cases, answers):
            with self.subTest(case=case, answer=ans):
                self.assertEqual(self.s.reachNumber(case), ans)
                
                # Check if negative values return same answer
                self.assertTrue(self.s.reachNumber(case) == \
                                self.s.reachNumber(-case))
                
if __name__ == '__main__':
    unittest.main()
