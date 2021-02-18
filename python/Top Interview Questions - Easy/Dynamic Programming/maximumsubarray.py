from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Returns the sum of the largest contiguous subarray.
        
        Params:
            nums - A list of integers.
            
        Returns:
            int - The sum of the largest subarray.
            
        Examples:   
            maxSubArray([-2,1,-3,4,-1,2,1,-5,4])   ->   6
            maxSubArray([1])                       ->   1
            maxSubArray([-1])                      ->   -1
            maxSubArray([0])                       ->   0
            maxSubArray([])                        ->   0
        '''
        if not nums:
            return 0
        
        high = nums[0]
        cur = 0
        for x in nums:
            cur += x
            high = max(high, cur)
            
            if cur < 0:
                cur = 0
                
        return high
