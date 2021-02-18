from collections import deque

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 7th, 2021.
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Returns the length of the longest substring with no repeating
        characters.
        
        Constraints:
            0 <= len(s) <= 5 * 10**4
            s consists of English letters, digits, symbols, and spaces
            
        Params:
            s - A string consisting of English letters, digits, symbols, and
                spaces.
                
        Returns:
            int - Length of longest substring without repeating characters.
            
        Examples:
            lengthOfLongestSubstring('abcabcbb')   ->   3
            lengthOfLongestSubstring('bbbbb')      ->   1
            lengthOfLongestSubstring('pwwkew')     ->   3
            lengthOfLongestSubstring('')           ->   0
        '''
        chars = set()
        substring = deque()
        longest = 0
        for idx, c in enumerate(s):
            longest = max(longest, len(chars))
            
            while c in chars:
                chars.remove(substring.popleft())
                
            substring.append(c)
            chars.add(c)
            
        longest = max(longest, len(chars))
        
        return longest
