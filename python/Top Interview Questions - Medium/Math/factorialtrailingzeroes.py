
class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        Returns the number of trailing zeroes in n!.
        
        Examples:
            trailingZeroes(0)    ->   0
            trailingZeroes(3)    ->   0
            trailingZeroes(5)    ->   1
            trailingZeroes(25)   ->   6
        '''
        zeroes = 0
        five_pow = 5
        while five_pow <= n:
            zeroes += n//five_pow
            five_pow *= 5
            
        return zeroes
