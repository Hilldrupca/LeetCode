
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 28th, 2021.
    '''
    def getSmallestString(self, n: int, k: int) -> str:
        '''
        Returns the lexicographically smallest string with length equal to n,
        and numeric value equal to k. A strings numeric value is the sum of
        each letters' index in the alphabet (1-indexed).
        
        Constraints:
            1 <= n <= 10**5
            n <= k <= 26 * n
            String will only contain lowercase English characters.
            
        Params;
            n - Length of desired string.
            
            k - Desired string value.
            
        Returns:
            str - Lexicographically smallest string of lenth n, and value k.
            
        Examples:
            getSmallestString(3, 27)   ->   'aay'
            getSmallestString(5, 73)   ->   'aaszz'
        '''
        if n * 26 == k:
            return n * 'z'
        k -= n
        z = k // 25
        a = n - z - 1
        return 'a'*a + chr(ord('a') + k%25) + 'z'*z
    
    
        '''
        Original implementation:
        
        alph = {x: chr(x+96) for x in range(1, 27)}
        while n:
            n -= 1
            min_x = max(1, k - n*26)
            k -= min_x
            res.append(alph[min_x])
            
        return ''.join(res)
        '''
        
