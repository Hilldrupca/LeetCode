import unittest, sys
sys.path.append('..')
from decodeways import Solution

class TestDecodeWays(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_num_decodings(self):
        case_one = "12"
        self.assertEqual(self.s.numDecodings(case_one), 2)
        
        case_two = "1111"
        self.assertEqual(self.s.numDecodings(case_two), 5)
        
        case_three = "226"
        self.assertEqual(self.s.numDecodings(case_three), 3)
        
        case_four = "190"
        self.assertEqual(self.s.numDecodings(case_four), 0)
        
        case_five = "110"
        self.assertEqual(self.s.numDecodings(case_five), 1)
        
        case_six = "2101"
        self.assertEqual(self.s.numDecodings(case_six), 1)
        
        case_seven = "111111111111111111111111111111111111111111111"
        self.assertEqual(self.s.numDecodings(case_seven), 1836311903)
        
        case_eight = '01'
        self.assertEqual(self.s.numDecodings(case_eight), 0)
        
if __name__ == '__main__':
    unittest.main()
