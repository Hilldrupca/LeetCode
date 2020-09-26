import unittest, sys
sys.path.append('..')
from matrixzeroes import Solution

class TestMatrixZeroes(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_set_zeroes(self):
        case_one = [[1,1,1],
                    [1,0,1],
                    [1,1,1]]
        self.s.setZeroes(case_one)
        self.assertEqual(case_one, [[1,0,1],
                                    [0,0,0],
                                    [1,0,1]])
        
        case_two = [[1,2,3,4],
                    [5,0,7,8],
                    [0,10,11,12],
                    [13,14,15,0]]
        self.s.setZeroes(case_two)
        self.assertEqual(case_two, [[0,0,3,0],
                                    [0,0,0,0],
                                    [0,0,0,0],
                                    [0,0,0,0]])
        
        case_three = [[0,1,2,0],
                      [3,4,5,2],
                      [1,3,1,5]]
        self.s.setZeroes(case_three)
        self.assertEqual(case_three, [[0,0,0,0],
                                      [0,4,5,0],
                                      [0,3,1,0]])
        
        case_four = [[0,1]]
        self.s.setZeroes(case_four)
        self.assertEqual(case_four, [[0,0]])
        
        case_five = [[7,0,0,5],
                     [9,2,0,8],
                     [2,6,5,1],
                     [1,9,3,8],
                     [5,3,4,6],
                     [5,2,0,2],
                     [4,3,5,1],
                     [5,2,4,4]]
        self.s.setZeroes(case_five)
        self.assertEqual(case_five, [[0,0,0,0],
                                     [0,0,0,0],
                                     [2,0,0,1],
                                     [1,0,0,8],
                                     [5,0,0,6],
                                     [0,0,0,0],
                                     [4,0,0,1],
                                     [5,0,0,4]])
        
if __name__ == '__main__':
    unittest.main()
