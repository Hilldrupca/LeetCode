from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for August 18th, 2020.
    '''
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        '''
        Return all non-negative integers of length N such that the absolute
        difference between every two consecutive digits is K.
        
        Note that every number in the answer must not have leading zeros except
        for the number 0 itself. For example, 01 has one leading zero and is
        invalid, but 0 is valid.
        '''
        # Length of 1 is just the digits 0 through 9
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        
        result = [1,2,3,4,5,6,7,8,9]
        
        for _ in range(N-1):
            if K:
                # Modified python implementation of itertools.product
                result = [10*x + x%10 - k for x in result for k in [K, -K]
                          if 0 <= x%10 - k < 10]
            
            # If K is 0, each numbered is attachecd to itself N times
            # N=2, k=0:  [11, 22, 33, ..., 99]
            else:
                result = [10*x + x%10 for x in result]
            
        return result
