import unittest, sys
sys.path.append('..')
from longestpalindromesubstring import Solution

class TestLongestPalindromeSubstring(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_longest_palindrome(self):
        self.assertEqual(self.s.longestPalindrome('babad'), 'aba')
        self.assertEqual(self.s.longestPalindrome('cbbd'), 'bb')
        
if __name__ == '__main__':
    unittest.main()
