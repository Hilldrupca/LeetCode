
class Solution:
    '''
    LeetCode Monthly Challenge problem for February 1st, 2021.
    '''
    def hammingWeight(self, n: int) -> int:
        '''
        Returns the number of 1 bits a given integer has.
        
        Params:
            n - An integer.
            
        Returns:
            int - The hamming weight of an integer.
            
        Examples:
            hammingWeight(11)           ->   3
            hammingWeight(128)          ->   1
            hammingWeight(4294967293)   ->   31
        '''
        res = 0
        while n:
            res += n & 1
            n >>= 1
            
        return res
