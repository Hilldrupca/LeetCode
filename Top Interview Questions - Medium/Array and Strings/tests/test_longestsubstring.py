import unittest, sys
sys.path.append('..')
from longestsubstring import Solution

class TestLongestSubstring(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().lengthOfLongestSubstring
        
    def test_length_of_longest_substring(self):
        self.assertEqual(self.s('abcabcbb'), 3)
        self.assertEqual(self.s('pwwkew'), 3)
        self.assertEqual(self.s(' '), 1)
        self.assertEqual(self.s('dvdf'), 3)
        
if __name__ == '__main__':
    unittest.main()
