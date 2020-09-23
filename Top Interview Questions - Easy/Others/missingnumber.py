from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Returns the number missing from the array. Assumes one number
        is guaranteed to be missing.
        
        Examples:
            missingNumber([3,0,1])               ->   2
            missingNumber([9,6,4,2,3,5,7,0,1])   ->   8
            missingNumber([3,2,1])               ->   0
        '''
        high = len(nums)
        sum_nat = high * (high + 1) / 2   # sum of first n natural numbers
        
        return sum_nat - sum(nums)
