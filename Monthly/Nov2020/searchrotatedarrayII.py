from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 20th, 2020.
    '''
    def search(self, nums: List[int], target: int) -> bool:
        '''
        Returns if the list contains a target number. The list must have been
        previously sorted. May be rotated any number of times, and may contain
        duplicates.
        
        Params:
            nums - A list of ascending integers shifted left an uknown amount.
            
            target - Integer to search for in nums.
            
        Returns:
            int - The index of target if it exists in nums, or -1 if not.
            
        Examples:
            search([2,5,6,0,0,1,2], 0)   ->   True
            search([2,5,6,0,0,1,2], 3)   ->   False
            search([4,5,6,7,0,1,2], 0)   ->   True
            search([1,3,1,1,1], 3)       ->   True
            search([1,1,3,1], 3)         ->   True
        '''
        if not nums or target is None:
            return False
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            
            if nums[mid] == target:
                return True
            
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid] :
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False
