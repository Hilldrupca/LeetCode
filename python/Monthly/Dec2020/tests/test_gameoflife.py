import unittest, sys
sys.path.append('..')
from gameoflife import Solution

class TestGameOfLife(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_game_of_life(self):
        case_one = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        self.s.gameOfLife(case_one)
        self.assertEqual(case_one, [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
        
        case_two = [[1,1],[1,0]]
        self.s.gameOfLife(case_two)
        self.assertEqual(case_two, [[1,1],[1,1]])
        
        case_three = []
        self.s.gameOfLife(case_three)
        self.assertEqual(case_three, [])
        
        case_four = [[],[],[]]
        self.s.gameOfLife(case_four)
        self.assertEqual(case_four, [[],[],[]])
        
        case_five = [[1],[1,0],[0,0]]
        self.s.gameOfLife(case_four)
        self.assertEqual(case_five, [[1],[1,0],[0,0]])
        
if __name__ == '__main__':
    unittest.main()
