import unittest, sys
sys.path.append('..')
from mergeintervals import Solution

class TestMergeIntervals(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_merge(self):
        case_one = [[1,3],[2,6],[8,10],[15,18]]
        self.assertEqual(self.s.merge(case_one),
                         [[1,6],[8,10],[15,18]])
        
        case_two = [[1,4],[4,5]]
        self.assertEqual(self.s.merge(case_two),
                         [[1,5]])
        
        case_three = [[1,4],[5,6]]
        self.assertEqual(self.s.merge(case_three),
                         [[1,4],[5,6]])
        
        case_four = [[1,4],[0,0]]
        self.assertEqual(self.s.merge(case_four),
                         [[0,0],[1,4]])
        
        case_five = [[2,3],[4,5],[6,7],[8,9],[1,10]]
        self.assertEqual(self.s.merge(case_five),
                         [[1,10]])
        
if __name__ == '__main__':
    unittest.main()
