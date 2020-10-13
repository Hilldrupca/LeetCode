import unittest, sys
sys.path.append('..')
from matrixsearch import Solution

class TestMatrixSearch(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_search_matrix(self):
        matrix = [[1,   4,  7, 11, 15],
                  [2,   5,  8, 12, 19],
                  [3,   6,  9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]]
        
        self.assertTrue(self.s.searchMatrix(matrix, 5))
        self.assertFalse(self.s.searchMatrix(matrix, 20))
        
        
        matrix = []
        self.assertFalse(self.s.searchMatrix(matrix, 1))
        
        matrix = [[]]
        self.assertFalse(self.s.searchMatrix(matrix, 1))
        
if __name__ == '__main__':
    unittest.main()
