import unittest, sys
sys.path.append('..')
from diagonaltraverse import Solution

class TestDiagonalTraverse(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_diagonal_order(self):
        case_one = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(self.s.findDiagonalOrder(case_one),
                         [1,2,4,7,5,3,6,8,9])
        
        case_two = [[1,2],[3,4],[5,6]]
        self.assertEqual(self.s.findDiagonalOrder(case_two),
                         [1,2,3,5,4,6])
        
        case_three = [[1],[2],[3]]
        self.assertEqual(self.s.findDiagonalOrder(case_three),
                         [1,2,3])
        
        case_four = [[1,2,3]]
        self.assertEqual(self.s.findDiagonalOrder(case_four),
                         [1,2,3])
        
        case_five = [[],[],[]]
        self.assertEqual(self.s.findDiagonalOrder(case_five), [])
        
        case_six = []
        self.assertEqual(self.s.findDiagonalOrder(case_six), [])
        
if __name__ == '__main__':
    unittest.main()
