from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Returns all possible permutations of a list.
        
        Example:
            permute([1,2,3])   ->   [(1,2,3),
                                     (1,3,2),
                                     (2,1,3),
                                     (2,3,1),
                                     (3,1,2),
                                     (3,2,1)]
        '''
        
        return list(permutations(nums, len(nums)))
    
        '''
        # Non-standard library solution
        
        res = []
        
        def helper(a: List[int] = [], k=0):
            if k == len(a):
                res.append(list(a))
            else:
                for i in range(k, len(a)):
                    a[k], a[i] = a[i], a[k]
                    helper(a, k+1)
                    a[k], a[i] = a[i], a[k]
                
        helper(nums)
        return res
        '''
