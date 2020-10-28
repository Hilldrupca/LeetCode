import unittest, sys
sys.path.append('..')
from summaryranges import Solution

class TestSummaryRanges(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_summary_range(self):
        case_one = [0,1,2,4,5,7]
        self.assertEqual(self.s.summaryRanges(case_one), ['0->2','4->5','7'])
        
        
        case_two = [-1]
        self.assertEqual(self.s.summaryRanges(case_two), ['-1'])
        
        
        case_three = [0]
        self.assertEqual(self.s.summaryRanges(case_three), ['0'])
        
        
        case_four = []
        self.assertEqual(self.s.summaryRanges(case_four), [])
        
if __name__ == '__main__':
    unittest.main()
