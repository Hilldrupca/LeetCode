from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge for October 15th, 2020.
    '''
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        In-place shifts a given list k steps right.
        
        Params:
            nums - A list of integers.
            
            k - Number of steps to shift right.
            
        Returns:
            None - In-place modification to nums.
            
        Examples:
            rotate([1,2,3,4,5,6,7], 3)   ->   list becomes [5,6,7,1,2,3,4]
            rotate([-1,-100,3,99], 2)    ->   list becomes [3,99,-1,-100]
        '''
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
