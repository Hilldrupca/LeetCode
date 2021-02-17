from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 17th, 2021.
    '''
    def maxArea(self, height: List[int]) -> int:
        '''
        Given a list of non-negative integers where each element represents a
        vertical line at point i with height n (i, n), returns the max area
        formed by two vertical lines.
        
        Constraints:
            n == len(height)
            2 <= n <= 3 * 10**4
            0 <= height[i] <= 3 * 10**4
            
        Params:
            height - A list of non-negative integers.
            
        Returns:
            int - The maximum area formed by two vertical lines.
            
        Example:
            maxArea([1,8,6,2,5,4,8,3,7])   ->   49
            maxArea([1,1])                 ->   1
            maxArea([4,3,2,1,4])           ->   16
            maxArea([1,2,1])               ->   2
        '''
        area = 0
        start, end = 0, len(height) - 1
        
        while start < end:
            temp = min(height[start], height[end])
            area = max(area, temp * (end - start))
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
        return area
