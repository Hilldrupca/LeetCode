from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 18th, 2021.
    '''
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        '''
        Given a list of integers, returns the number of arithmetic slices. An
        arithmetic slice is any contiguous slice of a list with at least three
        element, and the difference between any two consecutive elements is the
        same. The following are examples of arithmetic sequences:
        
            1, 3, 5, 7, 9
            7, 7, 7
            3, -1, -5, -9
            
        The following is NOT arithmetic:
        
            1, 1, 2, 5, 7
            
        Params:
            A - A list of integers.
            
        Returns:
            int - The number of arithmetic slices a given list contains.
            
        Examples:
            numberOfArithmeticSlices([1,2,3,4])      ->   3
            numberOfArithmeticSlices([1,3,5,7,9])    ->   6
            numberOfArithmeticSlices([7,7,7,7])      ->   3
            numberOfArithmeticSlices([3,-1,-5,-9])   ->   3
        '''
        res = 0
        diffs = [None]
        
        for i in range(1, len(A)):
            d = A[i] - A[i-1]
            
            if d != diffs[-1]:
                
                if (n := len(diffs)) >= 2:
                    res += ((n-1) * (n)) // 2
                
                diffs = []
                
            diffs.append(d)
            
        if (n := len(diffs)) >= 2:
            res += ((n-1) * (n)) // 2
            
        return res
