import unittest, sys
sys.path.append('..')
from songpairsdivisbysixty import Solution

class TestSongPairsDivisibleBySixty(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_num_pairs_divisible_by_60(self):
        cases = [[30,20,150,100,40],
                 [60,60,60],
                 [174,188,377,437,54,498,455,239,183,347,59,199,52,488,147,82],
                 [20,40],
                 [30,30,30],
                 [10],
                 []]
        
        answers = [3,3,2,1,3,0,0]
        
        for case, ans in zip(cases, answers):
            with self.subTest(case=case, answer=ans):
                self.assertEqual(self.s.numPairsDivisibleBy60(case),ans)
                
if __name__ == '__main__':
    unittest.main()
