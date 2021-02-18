import unittest, sys
sys.path.append('..')
from matrixdiagonalsort import Solution

class TestMatrixDiagonalSort(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_diagonal_sort(self):
        case_one = [[3,3,1,1],
                    [2,2,1,2],
                    [1,1,1,2]]
        
        self.assertEqual(self.s.diagonalSort(case_one),
                         [[1,1,1,1],
                          [1,2,2,2],
                          [1,2,3,3]])

if __name__ == '__main__':
    unittest.main()
