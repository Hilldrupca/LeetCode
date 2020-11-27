from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem November 27th, 2020.
    '''
    def canPartition(self, nums: List[int]) -> bool:
        '''
        Returns whether a list of positive integers contains two subsets whose
        sums are equal.
        
        Constraints:
            1 <= len(nums) <= 200
            1 <= nums[i] <= 100
        
        Params:
            nums - A list of positive integers.
            
        Returns:
            bool - Whether two subsets with equals sums exist in a list.
            
        Examples:
            canPartition([1,5,11,5])   ->   True
            canPartition([1,2,3,5])    ->   False
        '''
        if not nums:
            return False
        
        total = sum(nums)
        
        if total % 2:
            return False
        
        nums = sorted(nums, reverse=True)
        half = total//2
        
        for i in range(1, len(nums)):
            s = nums[0]
            
            for j in range(i, len(nums)):
                s += nums[j]
                if s > half:
                    s -= nums[j]
                if s == half:
                    return True
                
        return False
