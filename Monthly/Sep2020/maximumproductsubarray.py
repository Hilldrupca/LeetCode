from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 11th, 2020.
    
    TODO:
        Implement more optimized algorithm.
        
        Current implementation works, but runs very slowly on
        LeetCode's runtimes.
    '''
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Find the largest contiguous subarray product.
        
        Params:
            nums - List of integers.
            
        Returns:
            int - The maximum subarray product.
            
        Examples:
            maxProduct([2,3,-2,4])   ->   6
            maxProduct([-2,0,-1])    ->   0
            maxProduct([-4,-3])      ->   12
            maxProduct([0])          ->   0
            maxProduct([3,-1,4])     ->   4
        '''
        res = float('-inf')
        for x in range(len(nums)):
            cur = 1
            for y in range(x, len(nums)):
                cur *= nums[y]
                
                if cur > res:
                    res = cur
                
        return res
