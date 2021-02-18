import unittest, sys
sys.path.append('..')
from longestpalindromicsubstring import Solution

class TestLongestPalindromicSubstring(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_longest_palindrome(self):
        self.assertEqual(self.s.longestPalindrome('babad'), 'bab')
        
        self.assertEqual(self.s.longestPalindrome('cbbd'), 'bb')
        
        self.assertEqual(self.s.longestPalindrome('a'), 'a')
        
        self.assertEqual(self.s.longestPalindrome('ac'), 'a')
        
        self.assertEqual(self.s.longestPalindrome('aaaa'), 'aaaa')
        
        self.assertEqual(self.s.longestPalindrome(''), '')        
        
if __name__ == '__main__':
    unittest.main()
