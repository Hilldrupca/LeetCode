import unittest, sys
sys.path.append('..')
from zigzagconversion import Solution

class TestZigZagConversion(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_convert(self):
        test_str = 'zigzagpattern'
        
        self.assertEqual(self.s.convert(test_str, 1), 'zigzagpattern')
        
        self.assertEqual(self.s.convert(test_str, 3), 'zatnizgatrgpe')
        
        self.assertEqual(self.s.convert(test_str, 4), 'zpnigargatezt')
        
        
        self.assertEqual(self.s.convert(test_str, 0), 'zigzagpattern')
        self.assertEqual(self.s.convert('', 10), '')
        
if __name__ == '__main__':
    unittest.main()
