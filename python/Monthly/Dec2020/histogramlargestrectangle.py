from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 31st, 2020.
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Given a list of non-negative integers representing a histogram's bar
        height where the width of each bar is 1, returns the area of the
        largest rectangle.
        
        Disclaimer:
            At one point I was on roughly the right track to the current
            implementation, but ultimately needed help. Credit goes to the
            following GeeksforGeeks article:
            
            https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
        
        Constraints:
            0 <= heights[i]
        
        Params:
            heights - A list of non-negative integers.
            
        Returns:
            int - The area of the largest rectangle in the histogram.
            
        Examples:
            largestRectangleArea([2,1,5,6,2,3])   ->   10
            largestRectangleArea([2,1,2])         ->   3
            largestRectangleArea([5,4,1,2])       ->   8            
        '''
        largest = idx = 0
        stack = []
        while idx < len(heights):
            
            if not stack or heights[stack[-1]] < heights[idx]:
                stack.append(idx)
                idx += 1
                
            else:
                top = stack.pop()
                largest = max(largest,
                              (idx - stack[-1] - 1 if stack else idx) * heights[top])
                
        while stack:
            top = stack.pop()
            largest = max(largest,
                          (idx - stack[-1] - 1 if stack else idx) * heights[top])
        return largest
