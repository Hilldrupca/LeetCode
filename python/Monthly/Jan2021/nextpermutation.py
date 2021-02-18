from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 31st, 2021.
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        '''
        Given a list of non-negative integers, rearranges the list in-place to
        the lexicographically next greater permutation of numbers. If not
        possible, rearranges in the lowest possible order (sorted in ascending
        order).
        
        Constraints:
            1 <= len(nums) <= 100
            0 <= nums[i] <= 100
            
        Params:
            nums - A list of non-negative integers.
            
        Returns:
            None - In-place rearrangement to next permuation.
            
        Examples:
            nums = [1,2,3]
            nextPermuation(nums)   ->   nums == [1,3,2]
            
            nums = [3,2,1]
            nextPermuation(nums)   ->   nums == [1,2,3]
            
            nums = [5,4,7,5,3,2]
            nextPermuation(nums)   ->   nums == [5,5,2,3,4,7]
        '''
        i = j = 0
        for k in range(1, len(nums)):
            if nums[k] > nums[k-1]:
                i = k
            elif nums[i-1] < nums[k]:
                j = k
               
        if j > i:
            nums[i-1], nums[j] = nums[j], nums[i-1]
        else:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            
        nums[i:] = sorted(nums[i:])
