
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        Returns the hamming distance between two integers. The Hamming distance
        is the number of bits that are different between two integers.
        
        Examples:
            hammingDistance(x=1, y=4)    ->   2
                1   (0 0 0 1)
                4   (0 1 0 0)
                       ^   ^
                       
            hammingDistance(x=12, y=7)   ->   3
                12   (1 1 0 0)
                7    (0 1 1 1)
                      ^   ^ ^
        '''
        n = x^y
        weight = 0
        while n:
            prev = n
            n >>= 1
            if n < prev/2: weight += 1
            
        return weight
    
    
        # Easier to read implementation
        #return bin(x^y).count('1')
