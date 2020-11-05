import unittest, sys
sys.path.append('..')
from mincostmovechips import Solution

class TestMinCostMoveChips(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_min_cost_to_move_chips(self):
        case_one = [1,2,3]
        self.assertEqual(self.s.minCostToMoveChips(case_one), 1)
        
        case_two = [2,2,2,3,3]
        self.assertEqual(self.s.minCostToMoveChips(case_two), 2)
        
        case_three = [1,1000000000]
        self.assertEqual(self.s.minCostToMoveChips(case_three), 1)
        
        case_four = [1]
        self.assertEqual(self.s.minCostToMoveChips(case_four), 0)
        
        case_five = []
        self.assertEqual(self.s.minCostToMoveChips(case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
