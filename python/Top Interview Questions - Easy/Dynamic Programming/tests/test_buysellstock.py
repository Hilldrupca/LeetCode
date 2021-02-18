import unittest, sys
sys.path.append('..')
from buysellstock import Solution

class TestBuySellStock(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_profit(self):
        case_one = [7,1,5,3,6,4]
        self.assertEqual(self.s.maxProfit(case_one), 5)
        
        case_two = [7,6,4,3,1]
        self.assertEqual(self.s.maxProfit(case_two), 0)
        
        case_three = [1,2]
        self.assertEqual(self.s.maxProfit(case_three), 1)
        
if __name__ == '__main__':
    unittest.main()
