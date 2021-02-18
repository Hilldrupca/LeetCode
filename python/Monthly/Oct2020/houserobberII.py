from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 14th, 2020.
    '''
    def rob(self, nums: List[int]) -> int:
        '''
        Returns the maximum amount that can be robbed from houses on a street
        arranged in a circle. So the first and last houses are neighbors. If
        any two adjacent houses are robbed, the security systems will alert
        the police.
        
        Params:
            nums - A list of integers. Each integer represents how much money
                   that house has.
                   
        Returns:
            int - The maximum amount that can be robbed.
            
        Examples:
            rob([2,3,2])     ->   3
            rob([1,2,3,1])   ->   4
            rob([0])         ->   0
        '''
        if len(nums) == 1:
            return nums[0]
        
        # First run - exclude the last house
        prev = cur = 0
        for x in range(len(nums) -1):
            prev, cur = cur, max(cur, prev + nums[x])
            
        # Second run - exclude the first house
        prev = cur2 = 0
        for x in range(1, len(nums)):
            prev, cur2 = cur2, max(cur2, prev + nums[x])
            
        # Return the max of the two scenarios
        return max(cur, cur2)
