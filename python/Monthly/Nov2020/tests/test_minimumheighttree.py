import unittest, sys
sys.path.append('..')
from minimumheighttree import Solution

class TestMinimumHeightTree(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_min_height_tree(self):
        case_one = {'n': 4,
                    'edges': [[1,0],[1,2],[1,3]]}
        self.assertEqual(self.s.findMinHeightTrees(**case_one), [1])
        
        
        case_two = {'n': 6,
                    'edges': [[3,0],[3,1],[3,2],[3,4],[5,4]]}
        self.assertEqual(self.s.findMinHeightTrees(**case_two), [3,4])
        
        
        case_three = {'n': 1,
                      'edges': []}
        self.assertEqual(self.s.findMinHeightTrees(**case_three), [0])
        
        
        case_four = {'n': 2,
                     'edges': [[0,1]]}
        self.assertEqual(self.s.findMinHeightTrees(**case_four), [0,1])
        
        
        case_five = {'n': 8,
                     'edges': [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]]}
        self.assertEqual(self.s.findMinHeightTrees(**case_five), [0])
        
        
        case_six = {'n': 0,
                    'edges': [[0,1]]}
        self.assertEqual(self.s.findMinHeightTrees(**case_six), [])
        
        
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(self.s.findMinHeightTrees(1,[[0,1]]), [])
        
        self.assertEqual(self.s.findMinHeightTrees(1,[[1,0]]), [])
        
if __name__ == '__main__':
    unittest.main()
