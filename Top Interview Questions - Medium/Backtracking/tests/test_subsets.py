import unittest, sys
sys.path.append('..')
from subsets import Solution

class TestSubsets(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_subsets(self):
        answer = self.s.subsets([1,2,3])
        
        # in sorted order
        expected = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
        
        for exp in expected:
            self.assertIn(exp, answer)
            
        self.assertEqual(len(answer), len(expected))
        
if __name__ == '__main__':
    unittest.main()
