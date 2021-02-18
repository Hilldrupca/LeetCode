
class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Returns the number of '1' bits in an integer. (Hamming weight)
        
        Examples:
            hammingWeight(11)           ->   3
            hammingWeight(128)          ->   1
            hammingWeight(4294967293)   ->   31
        '''
        ones = 0
        while n:
            prev = n
            n >>= 1
            if n < prev/2: ones += 1
            
        return ones
    
    
    
        # Easier to read implementation
        #return bin(n).count('1')
