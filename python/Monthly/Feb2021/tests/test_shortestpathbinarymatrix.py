import unittest, sys
sys.path.append('..')
from shortestpathbinarymatrix import Solution

class TestShortestPathBinaryMatrix(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_shortest_path_binary_matrix(self):
        case_one = [[0,1],
                    [1,0]]
        
        self.assertEqual(self.s.shortestPathBinaryMatrix(case_one), 2)
        
        case_two = [[0,0,0],
                    [1,1,0],
                    [1,1,0]]
        
        self.assertEqual(self.s.shortestPathBinaryMatrix(case_two), 4)
        
        case_three = [[1,0,0],
                      [1,1,0],
                      [1,1,0]]
        
        self.assertEqual(self.s.shortestPathBinaryMatrix(case_three), -1)
        
if __name__ == '__main__':
    unittest.main()
