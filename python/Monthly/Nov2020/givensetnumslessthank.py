from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 22, 2020
    '''
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        '''
        Given a set of digits, returns the number of integers that can be
        generated that are less than or equal to n. Repeat digits are allowed.
        
        If digits = ['1','2','3'], and n = 23 possible integers are:
            
            1, 2, 3, 11, 12, 13, 21, 22, and 23
        
        Params:
            digits - A set of unique integers. Each element must be from '1' to
                     '9'.
            
            n - Target number than generated integers must be less than or
                equal to.
                
        Returns:
            int - Number of generated integers less than or equal to n.
            
        Examples:
            atMostNGivenDigitSet(["1","3","5","7"],
                                 100)               ->   20
            atMostNGivenDigitSet(["1","4","9"],
                                 1000000000)        ->   29523
            atMostNGivenDigitSet(["1","2","3","4","6","7","8","9"],
                                 67688637)          ->   12255070
            atMostNGivenDigitSet(["7"],
                                 8)                 ->   1
        '''
        if not digits or not n:
            return 0
        
        n = str(n)
        n_len = len(n)
        nums = 0
        for i in range(1, n_len):
            nums += len(digits)**i
            
        i, eq = 0, 1
        while i < n_len and eq:
            less = eq = 0
            for d in digits:
                if d < n[i]:
                    less += 1
                elif d == n[i]:
                    eq = 1
                    
            nums += less*len(digits)**(n_len-1-i)
            i += 1
            
        if eq:
            nums += 1
            
        return nums
