from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        In-place sort of a list of integers. List may only contain
        0's, 1's, and 2's.
        
        Params:
            nums - A list containing 0's, 1's, and 2's.
            
        Returns:
            None - In-place sort.
            
        Examples:
            sortColors([2,0,2,1,1,0])   ->   [0,0,1,1,2,2]
            sortColors([2,0,1])         ->   [0,1,2]
        """
        zero = idx = 0
        end = len(nums) - 1
        while idx <= end:
            if nums[idx] == 0:
                nums[zero], nums[idx] = nums[idx], nums[zero]
                zero += 1
                idx += 1
            elif nums[idx] == 2:
                nums[end], nums[idx] = nums[idx], nums[end]
                end -= 1
            else:
                idx += 1
