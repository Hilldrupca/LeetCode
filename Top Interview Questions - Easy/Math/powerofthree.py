 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        Determines if a number is a power of three.
        
        Examples:
            isPowerOfThree(27)   ->   True
            isPowerOfThree(0)    ->   False
            isPowerOfThree(9)    ->   True
            isPowerOfThree(45)   ->   False
        '''
        while n > 1:
            if n % 3 != 0:
                return False
            
            n /= 3
            
        return n == 1
