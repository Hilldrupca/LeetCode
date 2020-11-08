from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        '''
        Returns the given list of integers such as even numbers appear at the
        beginning, and odd numbers at the end. No other order is guaranteed.
        
        Params:
            A - A list of integers.
            
        Returns:
            List[int] - A list of integers sorted by parity.
            
        Example:
            sortArrayByParity([3,1,2,4])   ->   [4,2,1,3]
        '''
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] % 2:
                A[l], A[r] = A[r], A[l]
                r -= 1
            else:
                l += 1
                
        return A
