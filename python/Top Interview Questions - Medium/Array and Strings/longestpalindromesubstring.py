
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Returns the longest palindrome within a given string. If there exist
        two or more palindromes of the same length, whichever comes first
        aphabetically will be returned.
        
        Example:
            longestPalindrome('babad')   ->   'aba'
            longestPalindrome('cddb')    ->   'bb'
        '''
        longest = ''
        for i in range(len(s)):
            center = self._expand(i, i, s)
            mirror = self._expand(i, i+1, s)
            longest = max(center, mirror, longest, key=len)
        
        return longest
        
    def _expand(self, left: int, right: int, s: str):
        '''
        Helper function to expand from center indices.
        '''
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left+1:right]
