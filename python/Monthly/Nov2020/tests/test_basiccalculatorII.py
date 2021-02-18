import unittest, sys
sys.path.append('..')
from basiccalculatorII import Solution

class TestBasicCalculatorII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_calculate(self):
        case_one = '3+2*2'
        self.assertEqual(self.s.calculate(case_one), 7)
        
        case_two = ' 3/2 '
        self.assertEqual(self.s.calculate(case_two), 1)
        
        case_three = ' 3+5 / 2 '
        self.assertEqual(self.s.calculate(case_three), 5)
        
if __name__ == '__main__':
    unittest.main()
