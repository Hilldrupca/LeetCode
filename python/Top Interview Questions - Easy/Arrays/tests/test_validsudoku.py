import unittest, sys
sys.path.append('..')
from validsudoku import Solution

class TestValidSudoku(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().isValidSudoku
        
    def test_board_validity(self):
        case_one = [["5","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]]
        self.assertTrue(self.s(case_one))
        
        # Same as case_one except [0][0] changed from 5 -> 8
        case_two = [["8","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]]
        self.assertFalse(self.s(case_two))
        
if __name__ == '__main__':
    unittest.main()