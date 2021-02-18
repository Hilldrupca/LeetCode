import unittest, sys
sys.path.append('..')
from searchmatrix import Solution

class TestSearchMatrix(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_search_matrix(self):
        matrix = [[ 1, 3, 5, 7],
                  [10,11,16,20],
                  [23,30,34,50]]
        
        self.assertTrue(self.s.searchMatrix(matrix, 3))
        self.assertFalse(self.s.searchMatrix(matrix, 13))
        
        
        matrix = []
        self.assertFalse(self.s.searchMatrix(matrix, 0))
        
if __name__ == '__main__':
    unittest.main()
