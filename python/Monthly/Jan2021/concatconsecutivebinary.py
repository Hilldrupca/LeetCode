
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 27th, 2021.
    '''
    def concatenatedBinary(self, n: int) -> int:
        '''
        Given an integer n, return the decimal value of the binary string
        formed by concatenating the binary representations of 1 to n in order,
        modulo 10**9 + 7.
        
        Constraints:
            1 <= n <= 10**5
            
        Params:
            n - A positive integer.
            
        Returns:
            int - The decimal value of concatenated binary strings mod 10**9 + 7.
            
        Examples:
            concatenatedBinary(1)    ->   1
            concatenatedBinary(3)    ->   27
            concatenatedBinary(12)   ->   505379714
        '''
        binary = []
        for x in range(1, n+1):
            binary.append(bin(x)[2:])
            
        return int(''.join(binary), 2) % (10**9 +  7)
