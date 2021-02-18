import unittest, sys
sys.path.append('..')
from permutations import Solution

class TestPermutations(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
    
    def test_permute(self):
        answer = self.s.permute([1,2,3])
        expected = [(1,2,3),
                    (1,3,2),
                    (2,1,3),
                    (2,3,1),
                    (3,1,2),
                    (3,2,1)]
        
        for exp in expected:
            self.assertIn(exp, answer)
            
        self.assertEqual(len(expected), len(answer))
        
if __name__ == '__main__':
    unittest.main()
