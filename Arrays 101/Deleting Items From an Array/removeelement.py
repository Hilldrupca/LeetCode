from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        In-place removal of all instances of a number from a list of integers,
        and then returns the new length of the given list. Original order is
        not guaranteed.
        
        Params:
            nums - A list of integers.
            
            val - The integer to remove from nums.
            
        Returns:
            int - The length of nums after removal of all instances of val.
            
        Examples:
            nums = [3,2,2,3]
            removeElement(nums, 3)   ->   2, nums == [2,2]
            
            nums = [0,1,2,2,3,0,4,2]
            removeElement(nums, 2)   ->   5, nums == [0,1,0,4,3]
        '''
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
                del nums[-1]
            
        return len(nums)
