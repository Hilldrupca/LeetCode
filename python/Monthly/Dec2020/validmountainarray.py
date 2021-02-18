from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 10th, 2020.
    '''
    def validMountainArray(self, arr: List[int]) -> bool:
        '''
        Returns whether the given list of integers is a mountain array. A
        mountain array must have a length of at least three, and adhere to the
        following general structure:
        
            ... < arr[i-1] < arr[i] > arr[i+1] > ...
            
        Constraints:
            1 <= len(arr) <= 10**4
            0 <= arr[i] <= 10**4
            
        Params:
            arr - A list of integers.
            
        Returns:
            bool - Whether the array is a mountain array.
            
        Examples:
            validMountainArray([2,1])       ->   False
            validMountainArray([3,5,5])     ->   False
            validMountainArray([0,3,2,1])   ->   True
        '''
        if len(arr) < 3:
            return False
        
        up = down = 0
        for i in range(1,len(arr)):
            
            if arr[i-1] < arr[i] and not down:
                up += 1
            elif arr[i-1] > arr[i] and up:
                down += 1
            else:
                return False
            
        return up and down
