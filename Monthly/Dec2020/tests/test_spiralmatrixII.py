import unittest, sys
sys.path.append('..')
from spiralmatrixII import Solution

class TestSpiralMatrixII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_generate_matrix(self):
        self.assertEqual(self.s.generateMatrix(2),
                         [[1,2],[4,3]])
        
        self.assertEqual(self.s.generateMatrix(3),
                         [[1,2,3],[8,9,4],[7,6,5]])
        
        self.assertEqual(self.s.generateMatrix(0), [])
        
if __name__ == '__main__':
    unittest.main()
