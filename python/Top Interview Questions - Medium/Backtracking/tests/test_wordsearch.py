import unittest, sys
sys.path.append('..')
from wordsearch import Solution

class TestWordSearch(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_exist(self):
        board = [['A','B','C','E'],
                 ['S','F','C','S'],
                 ['A','D','E','E']]
        
        self.assertTrue(self.s.exist(board, 'ABCCED'))
        self.assertTrue(self.s.exist(board, 'SEE'))
        self.assertFalse(self.s.exist(board, 'see'))
        self.assertFalse(self.s.exist(board, 'ABCB'))
        
if __name__ == '__main__':
    unittest.main()
