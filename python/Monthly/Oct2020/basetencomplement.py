
class Solution:
    '''
    LeetCode Monthly Challenge for October 5th, 2020.
    '''
    def bitwiseComplement(self, N: int) -> int:
        '''
        Returns the complement of a given integer.
        
        Examples:
            bitwiseComplement(5)    ->   2
                5 in binary is '101' it's complement is '010' which is 2
                
            bitwiseComplement(7)    ->   0
                7 in binary is '111' it's complement is '000' which is 0
                
            bitwiseComplement(10)   ->   5
                10 in binary is '1010' it's complement is '0101' which is 5
        '''
        
        return N ^ (2**N.bit_length() -1) if N else 1
