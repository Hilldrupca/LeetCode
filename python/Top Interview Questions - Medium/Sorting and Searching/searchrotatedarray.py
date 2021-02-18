from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Given a list of integers that was sorted in ascending order that was
        then rotated an unknown number of times left, returns the index of a
        target number.
        
        Params:
            nums - A list of ascending integers shifted left an uknown amount.
            
            target - Integer to search for in nums.
            
        Returns:
            int - The index of target if it exists in nums, or -1 if not.
            
        Examples:
            search([4,5,6,7,0,1,2], 0)   ->   4
            search([4,5,6,7,0,1,2], 3)   ->   -1
            search([5,1,3], 3)           ->   2
            search([1], 0)               ->   -1
        '''
        if not nums:
            return -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid] :
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
