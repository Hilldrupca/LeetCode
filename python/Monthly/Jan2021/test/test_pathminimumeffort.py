import unittest, sys
sys.path.append('..')
from pathminimumeffort import Solution

class TestPathMinimumEffort(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_minimum_effort_path(self):
        case_one = [[1,2,2],
                     [3,8,2],
                     [5,3,5]]
        
        self.assertEqual(self.s.minimumEffortPath(case_one), 2)
        
        case_two = [[1,2,3],
                     [3,8,4],
                     [5,3,5]]
        
        self.assertEqual(self.s.minimumEffortPath(case_two), 1)
        
        case_three = [[1,2,1,1,1],
                     [1,2,1,2,1],
                     [1,2,1,2,1],
                     [1,2,1,2,1],
                     [1,1,1,2,1]]
        
        self.assertEqual(self.s.minimumEffortPath(case_three), 0)
        
if __name__ == '__main__':
    unittest.main()
