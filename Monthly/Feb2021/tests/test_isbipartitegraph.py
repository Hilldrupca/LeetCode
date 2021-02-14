import unittest, sys
sys.path.append('..')
from isbipartitegraph import Solution

class TestIsBipartiteGraph(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_is_bipartite(self):
        case_one = [[1,3],
                    [0,2],
                    [1,3],
                    [0,2]]
        
        self.assertTrue(self.s.isBipartite(case_one))
        
        case_two = [[1,2,3],
                    [0,2],
                    [0,1,3],
                    [0,2]]
        
        self.assertFalse(self.s.isBipartite(case_two))
        
        case_three = [[4],
                      [],
                      [4],
                      [4],
                      [0,2,3]]
        
        self.assertTrue(self.s.isBipartite(case_three))
        
        case_four = [[],
                     [2,4,6],
                     [1,4,8,9],
                     [7,8],
                     [1,2,8,9],
                     [6,9],
                     [1,5,7,8,9],
                     [3,6,9],
                     [2,3,4,6,9],
                     [2,4,5,6,7,8]]
        
        self.assertFalse(self.s.isBipartite(case_four))
        
if __name__ == '__main__':
    unittest.main()
