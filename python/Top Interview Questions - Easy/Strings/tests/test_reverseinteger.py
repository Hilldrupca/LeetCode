import unittest, sys
sys.path.append('..')
from reverseinteger import Solution

class TestReverseInteger(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = 123
        self.assertEqual(self.s.reverse(case_one), 321)
        
        case_two = -123
        self.assertEqual(self.s.reverse(case_two), -321)
        
        case_three = 120
        self.assertEqual(self.s.reverse(case_three), 21)
        
if __name__ == '__main__':
    unittest.main()
