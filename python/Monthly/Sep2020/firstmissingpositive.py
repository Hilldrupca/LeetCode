from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 30th, 2020.
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Returns the smallest missing positive integer.
        
        Examples:
            firstMissingPositive([1,2,0])       ->   3
            firstMissingPositive([3,4,-1,1])    ->   2
            firstMissingPositive([7,8,9])       ->   1
            firstMissingPositive([0,2,2,1,1])   ->   3
        '''
        nums.sort()
        lowest = 0
        for x in nums:
            if x - lowest > 1:
                return lowest + 1
            elif x > 0:
                lowest = x
                
        return lowest + 1
