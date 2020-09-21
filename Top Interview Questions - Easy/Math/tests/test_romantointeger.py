import unittest, sys
sys.path.append('..')
from romantointeger import Solution

class TestRomanToInteger(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_romanToInt(self):
        self.assertEqual(self.s.romanToInt('III'), 3)
        self.assertEqual(self.s.romanToInt('IV'), 4)
        self.assertEqual(self.s.romanToInt('IX'), 9)
        self.assertEqual(self.s.romanToInt('LVIII'), 58)
        self.assertEqual(self.s.romanToInt('MCMXCIV'), 1994)
        
if __name__ == '__main__':
    unittest.main()
