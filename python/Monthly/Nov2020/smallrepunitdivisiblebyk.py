
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 25th, 2020.
    '''
    def smallestRepunitDivByK(self, K: int) -> int:
        '''
        Given a positive integer K, returns the length of the smallest positive
        repunit consisting of only 1's that is divisble by K. Repunit examples:
        
            1, 11, 111, 1111, 11111, ...
        
        Params:
            K - An integer divisor.
            
        Returns:
            int - The length of the smallest dividend consisting only of ones.
                  Returns -1 if not such answer exists.
                  
        Examples:
            smallestRepunitDivByK(1)   ->   1    N = 1
            smallestRepunitDivByK(2)   ->   -1   No N exists
            smallestRepunitDivByK(3)   ->   3    N = 111
        '''
        if not K%2 or not K%5:
            return -1
        
        res, mod = 1, 0
        while mod := (mod * 10 + 1) % K:
            res += 1
            
        return res
