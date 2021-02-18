import unittest, sys
sys.path.append('..')
from countsay import Solution

class TestCountSay(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().countAndSay
        
    def test_equals(self):
        case_one = 1
        self.assertEqual(self.s(case_one), '1')
        
        case_two = 2
        self.assertEqual(self.s(case_two), '11')
        
        case_three = 3
        self.assertEqual(self.s(case_three), '21')
        
        case_four = 4
        self.assertEqual(self.s(case_four), '1211')
        
        case_five = 5
        self.assertEqual(self.s(case_five), '111221')
        
if __name__ == '__main__':
    unittest.main()
