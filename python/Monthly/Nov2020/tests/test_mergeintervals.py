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
        
        case_two = [[1,4],[2,3]]
        self.assertEqual(self.s.merge(case_two), [[1,4]])
        
        case_three = []
        self.assertEqual(self.s.merge(case_three), [])
        
if __name__ == '__main__':
    unittest.main()
