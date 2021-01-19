
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 19th, 2021.
    '''
    def longestPalindrome(self, s: str) -> str:
        '''
        Given a string, returns the longest substring palindrome.
        
        Constraints:
            1 <= len(s) <= 1000
            s consists of only digits and English letters (lower-case and/or
                upper-case)
                
        Params:
            s - A string containing digits, and/or English letters.
            
        Returns:
            str - The longest substring palindrome.
            
        Examples:
            longestPalindrome('babad')   ->   'bab'
            longestPalindrome('cbbd')    ->   'bb'
            longestPalindrome('a')       ->   'a'
            longestPalindrome('aaaa')    ->   'aaaa'
        '''
        if not s or len(s) == 1:
            return s
        
        longest, s_len = '', len(s)
        
        for i in range(s_len):
            sing = doub = ''
            
            # check for odd length palindromes
            l = r = i
            while l >= 0 and r < s_len and s[l] == s[r]:
                l -= 1
                r += 1
            sing = s[l+1:r]
                
            # check for even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < s_len and s[l] == s[r]:
                l -= 1
                r += 1
            doub = s[l+1:r]
            
            longest = max(longest, sing, doub, key=len)
            
        return longest
