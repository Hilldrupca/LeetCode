import unittest, sys
sys.path.append('..')
from factorialtrailingzeroes import Solution

class TestFactorialTrailingZeroes(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_trailing_zeroes(self):
        self.assertEqual(self.s.trailingZeroes(0), 0)
        self.assertEqual(self.s.trailingZeroes(3), 0)
        self.assertEqual(self.s.trailingZeroes(5), 1)
        self.assertEqual(self.s.trailingZeroes(25), 6)
        self.assertEqual(self.s.trailingZeroes(1000), 249)
        
if __name__ == '__main__':
    unittest.main()
