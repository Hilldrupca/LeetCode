from collections import Counter
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 4th, 2021.
    '''
    def findLHS(self, nums: List[int]) -> int:
        '''
        Given a list of integers, returns the length of the longest subsequence
        where the difference between the maximum and minimum values is 1. This
        may also be called the longest harmonious subsequence.
        
        Constraints:
            1 <= len(nums) <= 2 * 10**4
            -10**9 <= nums[i] <= 10**9
            
        Params:
            nums - A list of integers.
            
        Returns:
            int - The length of the longest harmonious subsequence.
            
        Examples:
            findLHS([1,3,2,2,5,2,3,7])   ->   5
            findLHS([1,2,3,4])           ->   2
            findLHS([1,1,1,1])           ->   0
        '''
        counts = Counter(nums)
        longest = 0
        
        for n, count in counts.items():
            
            if n + 1 in counts:
                longest = max(longest, count + counts[n+1])
                
        return longest
