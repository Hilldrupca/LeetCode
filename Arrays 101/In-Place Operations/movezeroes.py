from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        (In-place) Moves all zero elements to the end of the given list while
        maintaining the relative order of the non-zero elements.
        
        Params:
            nums - A list of integers.
            
        Returns:
            None - In-place operation.
            
        Example:
            nums = [0,1,0,3,12]
            moveZeroes(nums)   ->   nums == [1,3,12,0,0]
        '''
        front = 0
        for x in nums:
            if x:
                nums[front] = x
                front += 1
                
        while front < len(nums):
            nums[front] = 0
            front += 1
