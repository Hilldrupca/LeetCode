from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 21, 2020.
    '''
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if not A or len(A) == 1:
            return 0
        
        A = sorted(A)
        left, right = A[0] + K, A[-1] - K
        res = A[-1] - A[0]
        
        for i in range(len(A)-1):
            res = min(res,
                      max(A[i] + K, right) - min(A[i+1] - K, left)
                      )
            
        return res
