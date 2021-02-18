from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Find the indices of two integers that add up to the target number.
        
        Note: nums will always have exactly one solution
        
        Params:
            nums - list of integers
            
            target - target integer for two elements in nums to add up to
            
        Returns:
            list of indices who's elemnts add up to target number
        '''
        minus_idx = {}
        
        for idx, n in enumerate(nums):
            if n not in minus_idx:
                minus_idx[target - n] = idx
            
            else:
                return [minus_idx[n], idx]
