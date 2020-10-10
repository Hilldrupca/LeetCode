import unittest, sys
sys.path.append('..')
from arrowstoburstballoons import Solution

class TestArrowsToBurstBalloons(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().findMinArrowShots
    
    def test_find_min_arrow_shots(self):
        self.assertEqual(self.s([[10,16],[2,8],[1,6],[7,12]]), 2)
        
        self.assertEqual(self.s([[1,2],[3,4],[5,6],[7,8]]), 4)
        
        self.assertEqual(self.s([[1,2],[2,3],[3,4],[4,5]]), 2)
        
        self.assertEqual(self.s([[1,2]]), 1)
        
        self.assertEqual(self.s([[2,3],[2,3]]), 1)
        
        self.assertEqual(self.s([[9,12],[1,10],[4,11],[8,12],
                                 [3,9],[6,9],[6,7]]), 2)
        
if __name__ == '__main__':
    unittest.main()
