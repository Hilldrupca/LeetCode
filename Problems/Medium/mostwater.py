from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Returns the maximum rectangular area given a list of wall heights. The
        container is generated by any two wall heights, and the width is the
        difference between their index positions.
        
        Params:
            height - A list of integers.
            
        Returns:
            int - The most water that can be contained.
            
        Examples:
            maxArea([1,8,6,2,5,4,8,3,7])   ->   49
            maxArea([1,1])                 ->   1
            maxArea([4,3,2,1,4])           ->   16
            maxArea([1,2,1])               ->   2
        '''
        if len(height) < 2:
            return 0
        
        l, r = 0, len(height) - 1
        most_water = 0
        while l < r:
            left, right = height[l], height[r]
            most_water = max(most_water,
                             min(left, right) * (r-l))
            
            if left <= right:
                while l < r and height[l] <= left:
                    l += 1
            else:
                while l < r and height[r] <= right:
                    r -= 1
                    
        return most_water