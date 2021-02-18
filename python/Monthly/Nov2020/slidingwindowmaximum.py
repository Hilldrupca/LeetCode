from typing import List
from collections import deque

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 28th, 2020.
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Returns the max sliding window of a given list of integers. The max
        sliding window is a list of maximum elements for each sliding window of
        size k over a list.
        
        Params:
            nums - A list of integers
            
            k - An integer window size.
            
        Returns:
            List[int] - The max sliding window.
            
        Exampes:
            maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)   ->   [3,3,5,5,6,7]
            maxSlidingWindow([1,-1], 1)                ->   [1,-1]
            maxSlidingWindow([5,4,3,2,1], 3)           ->   [5,4,3]
        '''
        if not nums or not k:
            return []
        
        res = []
        queue = deque(maxlen=k)
        
        for i in range(k-1):
            
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
                
            queue.append(i)
        
        for i in range(k-1, len(nums)):
            
            # Remove indices outside of current window
            while queue and queue[0] <= i - k:
                queue.popleft()
                
            # Remove indices whose elements are lower than the current
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
                
            queue.append(i)
            
            res.append(nums[queue[0]])
            
        return res
