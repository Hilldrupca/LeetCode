import unittest, sys
sys.path.append('..')
from houserobber import Solution

class TestHouseRobber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_rob(self):
        case_one = [1,2,3,1]
        self.assertEqual(self.s.rob(case_one), 4)
        
        case_two = [2,7,9,3,1]
        self.assertEqual(self.s.rob(case_two), 12)
        
        case_three = [2,1,1,2]
        self.assertEqual(self.s.rob(case_three), 4)
        
if __name__ == '__main__':
    unittest.main()
