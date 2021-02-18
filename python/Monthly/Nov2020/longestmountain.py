from typing import List

class Solution:
    '''
    LeetCode Monthly Challegen problem for November 16th, 2020.
    '''
    def longestMountain(self, A: List[int]) -> int:
        '''
        Returns the length of the longest contiguous mountain. A mountain is
        any subarray such that ...< A[n-1] < A[n] > A[n+1] >... holds true.
        
        I've also provided a more readable version at the bottom. According to
        LeetCode results, it is slightly slower.
        
        Params;
            A - A list of integers.
            
        Returns:
            int - The length of the longest mountain.
            
        Examples:
            longestMountain([2,1,4,7,3,2,5])   ->   5
            longestMountain([1,2,1])           ->   3
            longestMountain([2,2,2])           ->   0
            longestMountain([3,2,1])           ->   0
            longestMountain([1,2,3])           ->   0
        '''
        mountain = cur = 0
        ascend = True
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                if ascend:
                    cur += 1
                else:
                    # reset cur count if start of new mountain
                    ascend = True
                    mountain = max(mountain, cur)
                    cur = 1
                    
            elif A[i-1] > A[i] and cur:
                ascend = False
                cur += 1
            
            # reset if plateau, not strictly increasing or decreasing
            elif A[i-1] == A[i]:
                # account for mountain preceeding plateau
                if not ascend:
                    mountain = max(mountain, cur)
                    ascend = True
                cur = 0
        
        # check for trailing mountain
        if not ascend:
            mountain = max(mountain, cur)
        
        return mountain + 1 if mountain else 0
    
    
        '''
        mountain = i = 0
        while i < len(A)-2:
            
            up = 0
            while i < len(A)-1 and A[i] < A[i+1]:
                i += 1
                up += 1
                
            down = 0
            while i < len(A)-1 and A[i] > A[i+1]:
                i += 1
                down += 1
                
            if up and down:
                mountain = max(mountain, up + down + 1)
                
            while i < len(A) -1 and A[i] == A[i+1]:
                i += 1
            
        return mountain
        '''
