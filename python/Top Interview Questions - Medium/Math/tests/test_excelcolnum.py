import unittest, sys
sys.path.append('..')
from excelcolnum import Solution

class TestExcelColNum(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_title_to_number(self):
        case_one = 'A'
        self.assertEqual(self.s.titleToNumber(case_one), 1)
        
        
        case_two = 'AB'
        self.assertEqual(self.s.titleToNumber(case_two), 28)
        
        
        case_three = 'ZY'
        self.assertEqual(self.s.titleToNumber(case_three), 701)
        
        
        case_four = 'FXSHRXW'
        self.assertEqual(self.s.titleToNumber(case_four), 2147483647)
        
if __name__ == '__main__':
    unittest.main()
