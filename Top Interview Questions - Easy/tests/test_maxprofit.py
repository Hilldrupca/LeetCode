import unittest, sys
sys.path.append('..')
from maxprofit import Solution

class TestMaxProfit(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        
        case_one = [7,1,5,3,6,2]
        self.assertEquals(self.s.maxProfit(case_one),7)
        
        case_two = [1,2,3,4,5]
        self.assertEquals(self.s.maxProfit(case_two), 4)
        
        case_three = [7,6,4,3,1]
        self.assertEquals(self.s.maxProfit(case_three), 0)
                          
if __name__ == '__main__':
    unittest.main()
