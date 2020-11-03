import unittest, sys
sys.path.append('..')
from consecutivecharacters import Solution

class TestConsectiveCharacters(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_power(self):
        case_one = 'leetcode'
        self.assertEqual(self.s.maxPower(case_one), 2)
        
        
        case_two = 'hooraaaaaaaaaaay'
        self.assertEqual(self.s.maxPower(case_two), 11)
        
        
        case_three = 'tourist'
        self.assertEqual(self.s.maxPower(case_three), 1)
        
        
        case_four = 'cc'
        self.assertEqual(self.s.maxPower(case_four), 2)
        
        
        case_five = ''
        self.assertEqual(self.s.maxPower(case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
