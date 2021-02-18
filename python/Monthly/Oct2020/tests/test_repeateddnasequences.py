import unittest, sys
sys.path.append('..')
from repeateddnasequences import Solution

class TestRepeatedDnaSubsequences(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().findRepeatedDnaSequences
        
    def test_find_repeated_dna_subsequences(self):
        case_one = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
        ans_one = self.s(case_one)
        exp_ans = ["AAAAACCCCC","CCCCCAAAAA"]
        
        for s in exp_ans:
            self.assertIn(s, ans_one)
            
        case_two = 'AAAAAAAAAAAAA'
        self.assertEqual(self.s(case_two), ['AAAAAAAAAA'])
        
        self.assertEqual(self.s(""), [])
        
if __name__ == '__main__':
    unittest.main()
