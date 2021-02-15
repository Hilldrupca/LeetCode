from heapq import heapify, nsmallest
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 15th, 2021.
    '''
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        '''
        Given a list of binary lists, returns the k strongest indices sorted by
        strength. A rows strength is equal to the sum of its elements.
        
        Constraints:
            m == len(mat)
            n == len(mat[i])
            2 <= n, m <= 100
            1 <= k <= m
            matrix[i][j] is eight 0 or 1
            
        Params:
            mat - A binary matrix, eg a list of binary lists.
            
            k - Number of strongest row indices to return.
            
        Returns:
            List[int] - The indices of the k strongest rows, sorted by strength.
            
        Examples:
            kwargs = {'mat': [[1,1,0,0,0],
                              [1,1,1,1,0],
                              [1,0,0,0,0],
                              [1,1,0,0,0],
                              [1,1,1,1,1]],
                      'k': 3}
                      
            kWeakestRows(**kwargs)   ->   [2,0,3]
            
            kwargs = {'mat': [[1,0,0,0],
                              [1,1,1,1],
                              [1,0,0,0],
                              [1,0,0,0]],
                      'k': 2}
                      
            kWeakestRows(**kwargs)   ->   [0,2]
        '''
        sum_idx = []
        for i in range(len(mat)):
            sum_idx.append((sum(mat[i]), i))
            
        heapify(sum_idx)
        
        return [i for _, i in nsmallest(k, sum_idx)]
