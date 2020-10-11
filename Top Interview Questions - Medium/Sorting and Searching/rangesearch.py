from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Given a sorted list of integers, returns the start and end indices of
        target. 
        
        Intended performance - O(logn)
        
        Params:
            nums - A list of integers in ascending order.
            
            target - The target number to look for.
            
        Returns:
            List[int] - The start and end indices of target if it exists in
                        nums. Returns [-1,-1] if target cannot be found.
                        
        Examples:
            searchRange([5,7,7,8,8,10], 8)   ->   [3,4]
            searchRange([5,7,7,8,8,10], 6)   ->   [-1,-1]
            searchRange([], 0)               ->   [-1,-1]
            searchRange([3,3,3], 3)          ->   [0,2]
        '''
        
        # Perform binary search looking for leftmost index of target
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
        
        
        # If target is greater than all entries in nums, start will equal
        # len(nums).
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        
        # Perform binary search starting from leftmost index of target,
        # looking for rightmost index
        left, end = start, len(nums)
        while start < end:
            mid2 = (start + end)//2
            if nums[mid2] > target:
                end = mid2
            else:
                start = mid2 + 1
                
        return [left, end-1]
