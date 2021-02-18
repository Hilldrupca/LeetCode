
class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        Reveres the bits of a 32 bit unsigned integer.
        
        Examples:
            reverseBits(43261596)     ->   964176192
                
                Original = 00000010100101000001111010011100
                Reversed = 00111001011110000010100101000000
            
            reverseBits(4294967293)   ->   3221225471
                
                Original = 11111111111111111111111111111101
                Reversed = 10111111111111111111111111111111
        '''
        bits = format(n, '032b')
        return int(bits[::-1], 2)
