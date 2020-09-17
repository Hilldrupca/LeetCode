from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Returns the maximum amount of money you can rob without alerting the
        police. No two adjacent houses can be robbed o the same night.
        
        Params:
            nums - A list of integers representing money in each house.
            
        Returns:
            int - The high amount you can rob for the night.
            
        Examples:
            rob([1,2,3,1])     ->   4
            rob([2,7,9,3,1])   ->   12
            rob([2,1,1,2])     ->   4
        '''
        prev = cur = 0
        for x in nums:
            prev, cur = cur, max(prev + x, cur)
            
        return cur
