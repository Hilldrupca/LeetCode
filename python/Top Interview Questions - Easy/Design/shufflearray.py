from typing import List
from random import shuffle as rs

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.rand = list(nums)
        
    def reset(self) -> List[int]:
        '''
        Returns the original list of numbers unaltered.
        '''
        return self.nums
    
    def shuffle(self) -> List[int]:
        '''
        Returns a random shuffling of the list of numbers.
        '''
        rs(self.rand)
        return self.rand
