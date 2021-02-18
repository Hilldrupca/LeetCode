import unittest, sys
sys.path.append('..')
from coinchange import Solution

class TestCoinChange(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_coin_change(self):
        case_one = {'coins': [1,2,5],
                    'amount': 11}
        self.assertEqual(self.s.coinChange(**case_one), 3)
        
        
        case_two = {'coins': [2],
                    'amount': 3}
        self.assertEqual(self.s.coinChange(**case_two), -1)
        
        
        case_three = {'coins': [1],
                      'amount': 0}
        self.assertEqual(self.s.coinChange(**case_three), 0)
        
        
        case_four = {'coins': [1],
                     'amount': 1}
        self.assertEqual(self.s.coinChange(**case_four), 1)
        
        
        case_five = {'coins': [1],
                     'amount': 2}
        self.assertEqual(self.s.coinChange(**case_five), 2)
        
        
        case_six = {'coins': [2,5,10,1],
                    'amount': 27}
        self.assertEqual(self.s.coinChange(**case_six), 4)
        
        
        case_seven = {'coins': [186,419,83,408],
                      'amount': 6249}
        self.assertEqual(self.s.coinChange(**case_seven), 20)
        
if __name__ == '__main__':
    unittest.main()
