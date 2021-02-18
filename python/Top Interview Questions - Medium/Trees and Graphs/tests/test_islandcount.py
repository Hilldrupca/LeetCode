import unittest, sys
sys.path.append('..')
from islandcount import Solution

class TestIslandCount(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_num_islands(self):
        case_one = [['1','1','0','0','0'],
                    ['1','1','0','0','0'],
                    ['0','0','1','0','0'],
                    ['0','0','0','1','1']]
        
        self.assertEqual(self.s.numIslands(case_one), 3)
        
        
        case_two = [["0","1","0"],
                    ["1","0","1"],
                    ["0","1","0"]]
        
        self.assertEqual(self.s.numIslands(case_two), 4)
        
        
        case_three = [["1","1","1","1","0"],
                      ["1","1","0","1","0"],
                      ["1","1","0","0","0"],
                      ["0","0","0","0","0"]]
        
        self.assertEqual(self.s.numIslands(case_three), 1)
        
        
        case_four = []
        
        self.assertEqual(self.s.numIslands(case_four), 0)
        
if __name__ == '__main__':
    unittest.main()
