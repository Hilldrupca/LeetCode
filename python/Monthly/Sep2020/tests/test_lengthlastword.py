import unittest, sys
sys.path.append('..')
from lengthlastword import Solution

class TestLengthLastWord(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_lengths(self):
        case_one = 'Hello World'
        self.assertEqual(self.s.lengthOfLastWord(case_one), 5)
        
        case_two = ''
        self.assertEqual(self.s.lengthOfLastWord(case_two), 0)
        
        case_three = ' '
        self.assertEqual(self.s.lengthOfLastWord(case_three), 0)
        
        case_four = 'b   a   '
        self.assertEqual(self.s.lengthOfLastWord(case_four), 1)
        
if __name__ == '__main__':
    unittest.main()
