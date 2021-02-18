import unittest, sys
sys.path.append('..')
from bullsandcows import Solution

class TestBullsAndCows(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_hints(self):
        case_one = {'secret': '1807', 'guess': '7810'}
        self.assertEqual(self.s.getHint(**case_one), '1A3B')
        
        case_two = {'secret': '1123', 'guess': '0111'}
        self.assertEqual(self.s.getHint(**case_two), '1A1B')
        
        case_three = {'secret': '1122', 'guess': '2211'}
        self.assertEqual(self.s.getHint(**case_three), '0A4B')
        
if __name__ == '__main__':
    unittest.main()
