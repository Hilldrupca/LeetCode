
class Solution:
    '''
    LeetCode Monthly Challenge problem for December 26th, 2020.
    '''
    def numDecodings(self, s: str) -> int:
        '''
        Given a non-empty string encoded to digits, returns the total
        number of ways to decode it. Integers decode to the following pattern:
        
            1 -> A
            2 -> B
            3 -> C
            ...
            26 -> Z
            
        Constraints:
            1 <= s.length <= 100
            s contains only digits and may contain leading zero(s)
            
        Params:
            s - A string of integer digits.
            
        Returns:
            int - Number of ways to decode the encoded string.
            
        Examples:
            numDecodings('12')    ->   2
            numDecodings('226')   ->   3
            numDecodings('10')    ->   1
            numDecodings('01')    ->   0
        '''        
        if not s or s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, len(s)+1):
            if s[i-1:i] != '0':
                dp[i] += dp[i-1]
                
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[-1]
