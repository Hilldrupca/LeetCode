from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        Returns the sum of three integers in nums that is closest to target.
        
        Params:
            nums - A list of integers. Will raise an error if length is not
                   at least 3.
            
            target - Target integer of summation.
            
        Returns:
            int - The sum closest to target.
            
        Examples:
            threeSumClosest([-1,2,1,-4], 1)   ->   2
            threeSumClosest([0,1,1,2], 2)     ->   2
        '''
        if len(nums) < 3:
            raise ValueError(
                f'List length must be at least 3, got {len(nums)}.')
        
        nums = sorted(nums)
        close = res = float('inf')
        
        for l in range(len(nums)-2):
            left = nums[l]
            
            m, r = l + 1, len(nums)-1
            
            while m < r:
                three_sum = nums[l] + nums[m] + nums[r]
                
                if three_sum < target:
                    if target - three_sum < close:
                        close = target - three_sum
                        res = three_sum
                    m += 1
                elif three_sum > target:
                    if three_sum - target < close:
                        close = three_sum - target
                        res = three_sum
                    r -= 1
                else:
                    return three_sum
                    
        return res
