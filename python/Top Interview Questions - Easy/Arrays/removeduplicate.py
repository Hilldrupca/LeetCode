from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Given a sorted array nums, remove the duplicates in-place such that
        each element appear only once and return the new length.

        Do not allocate extra space for another array, you must do this by
        modifying the input array in-place with O(1) extra memory.
        
        It doesn't matter what you leave beyond the returned length.
        
        
        Params:
            nums - a list of ints
            
        Returns:
            int - the last index+1 of nums for unique and sorted items.
            
        Examples:
            removeDuplicates([1,1,2]) returns 2, with the first two
                elements of nums being modified to [1,2].
            
            removeDuplicates([0,0,1,1,1,2,2,3,3,4]) returns 5, with the first
                five elements of nums being modified to [0,1,2,3,4]
        '''
        
        # Get unique numbers
        num_set = set(nums)
        length = len(num_set)
        
        # Set beginning elements of nums to the unique numbers
        for x, num in zip(range(length), num_set):
            nums[x] = num
        
        # Sort beginning numbers
        nums[:length] = sorted(nums[:length])
        
        return length
