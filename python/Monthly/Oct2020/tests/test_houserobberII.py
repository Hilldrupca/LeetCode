import unittest, sys
sys.path.append('..')
from houserobberII import Solution

class TestHouseRobberII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_rob(self):
        case_one = [2,3,2]
        self.assertEqual(self.s.rob(case_one), 3)
        
        
        case_two = [1,2,3,1]
        self.assertEqual(self.s.rob(case_two), 4)
        
        
        case_three = [0]
        self.assertEqual(self.s.rob(case_three), 0)
        
        
        case_four = []
        self.assertEqual(self.s.rob(case_four), 0)
        
if __name__ == '__main__':
    unittest.main()
