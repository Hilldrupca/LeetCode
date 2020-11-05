from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        '''
        Returns whether a given list of integers is a mountain array. A 
        mountain array is a list of integers that has at most one peak with
        strictly increaseing left side, and strictly decreasing right side.
        
        Params:
            A - A list of integers.
            
        Returns:
            bool - If a list of integers is a mountain array.
        
        Examples:
            validMountainArray([2,1])       ->   False
            validMountainArray([3,5,5])     ->   False
            validMountainArray([0,3,2,1])   ->   True
            validMountainArray([1])         ->   False
        '''
        if len(A) < 3:
            return False
        
        inc = dec = None
        for i in range(1, len(A)):
            if A[i] > A[i-1] and not dec:
                inc = True
            elif A[i] < A[i-1] and inc:
                dec = True
            else:
                return False
            
        return dec is not None
