from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Returns the element that appears more than len(nums)/2 times.
        '''
        return sorted(nums)[len(nums)//2]
