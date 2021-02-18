from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Returns the length of a given list of integers after removing duplicate
        elements in-place.
        
        Params:
            nums - A list of integers.
            
        Returns:
            int - The new length of nums.
            
        Examples:
            nums = [1,1,2]
            removeDuplicates(nums)   ->   2, nums == [1,2]
            
            nums = [0,0,1,1,1,2,2,3,3,4]
            removeDuplicates(nums)   ->   5, nums == [0,1,2,3,4]
        '''
        prev_idx = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[prev_idx]:
                prev_idx += 1
                nums[prev_idx] = nums[i]
                
        while len(nums) > prev_idx + 1:
            nums.pop()
            
        return prev_idx + 1
