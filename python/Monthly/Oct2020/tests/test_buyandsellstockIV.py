import unittest, sys
sys.path.append('..')
from buyandsellstockIV import Solution

class TestBuyAndSellStockIV(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_profit(self):
        case_one = {'k': 2,
                    'prices': [2,4,1]}
        
        self.assertEqual(self.s.maxProfit(**case_one), 2)
        
        
        case_two = {'k': 2,
                    'prices': [3,2,6,5,0,3]}
        
        self.assertEqual(self.s.maxProfit(**case_two), 7)
        
        
        case_three = {'k': 2,
                      'prices': [1,2,4]}
        
        self.assertEqual(self.s.maxProfit(**case_three), 3)
        
        
        case_four = {'k': 1,
                     'prices': [1,2]}
        
        self.assertEqual(self.s.maxProfit(**case_four), 1)
        
        
        case_five = {'k': 2,
                     'prices': [2,2,5]}
        
        self.assertEqual(self.s.maxProfit(**case_five), 3)
        
        
        case_six = {'k': 3,
                    'prices': [8,6,4,3,3,2,3,5,8,3,8,2,6]}
        
        self.assertEqual(self.s.maxProfit(**case_six), 15)
        
if __name__ == '__main__':
    unittest.main()
