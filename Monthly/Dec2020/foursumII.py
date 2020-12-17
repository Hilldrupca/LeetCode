from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 17th, 2020.
    '''
    def fourSumCount(self, A: List[int], B: List[int],
                     C: List[int], D: List[int]) -> int:
        '''
        Returns how many combinations of A[i] + B[j] + C[k] + D[l] sum to zero.
        Empty lists are treated the same as [0], unless all are empty.
        
        Constraints:
            Lengths of A, B, C, and D are equal
            Integers range from -2**28 to 2**28 - 1
            Result guaranteed to be at most 2**31 - 1
            
        Params;
            A - A list of integers.
            
            B - A list of integers.
            
            C - A list of integers.
            
            D - A list of integers.
            
        Returns:
            int - The number of combinations whose sum is zero.
            
        Example:
            A = [1,2]
            B = [-2,-1]
            C = [-1,2]
            D = [0,2]
            
            fourSumCount(A,B,C,D)   ->   2
        '''
        # If all lists are empty
        if not A and not B and not C and not D:
            return 0
        
        # Populate empty lists with a single 0
        # so a result can still be calculated
        if not A: A = [0]
        if not B: B = [0]
        if not C: C = [0]
        if not D: D = [0]
        
        sum_ab = {}
        get = sum_ab.get
        for a in A:
            for b in B:
                sum_ab[a+b] = get(a+b,0) + 1
                
        res = 0
        for c in C:
            for d in D:
                res += get(-c-d,0)
                
        return res
