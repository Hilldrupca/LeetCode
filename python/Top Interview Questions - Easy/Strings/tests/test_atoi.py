import unittest, sys
sys.path.append('..')
from atoi import Solution

class TestAtoi(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().myAtoi
        
    def test_equals(self):
        case_one = '42'
        self.assertEqual(self.s(case_one), 42)
        
        case_two = '    -42'
        self.assertEqual(self.s(case_two), -42)
        
        case_three = '3.14'
        self.assertEqual(self.s(case_three), 3)
        
        case_four = '+-42'
        self.assertEqual(self.s(case_four), 0)
        
        case_five = 'Jan 1'
        self.assertEqual(self.s(case_five), 0)
        
if __name__ == '__main__':
    unittest.main()
