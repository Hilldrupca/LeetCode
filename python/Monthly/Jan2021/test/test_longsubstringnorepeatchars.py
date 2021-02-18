import unittest, sys
sys.path.append('..')
from longsubstringnorepeatchars import Solution

class TestLongSubstringNoRepeatChars(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_length_of_longest_substring(self):
        case_one = 'abcabcbb'
        self.assertEqual(self.s.lengthOfLongestSubstring(case_one), 3)
        
        case_two = 'bbbbb'
        self.assertEqual(self.s.lengthOfLongestSubstring(case_two), 1)
        
        case_three = 'pwwkew'
        self.assertEqual(self.s.lengthOfLongestSubstring(case_three), 3)
        
        case_four = ''
        self.assertEqual(self.s.lengthOfLongestSubstring(case_four), 0)
        
        case_five = 'dvdf'
        self.assertEqual(self.s.lengthOfLongestSubstring(case_five), 3)
        
        case_six = 'tmmzuxt'
        self.assertEqual(self.s.lengthOfLongestSubstring(case_six), 5)
        
if __name__ == '__main__':
    unittest.main()
