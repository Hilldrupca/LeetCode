from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 21, 2021.
    '''
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        '''
        Returns the most competitve subsequence of length k. Subsequence (a) is
        more competitive than subsequence (b), if at the first position where
        they differ (a) has a number less than (b). [1,3,4] is more competitive
        than [1,3,5]
        
        Constraints:
            1 <= len(nums) <= 10**5
            0 <= nums[i] <= 10**9
            1 <= k <= len(nums)
            
        Params;
            nums - A list of positive integers.
            
            k - A positive integer less than or equal length of nums.
            
        Returns:
            List[int] - Most competitive subsequence.
            
        Examples:
            mostCompetitive([3,5,2,6], 2)           ->   [2,6]
            mostCompetitive([2,4,3,3,5,4,9,6], 4)   ->   [2,3,3,4]
        '''
        res = []
        
        for i, x in enumerate(nums):
            while res and res[-1] > x and len(nums) - i - 1 >= k - len(res):
                res.pop()
            
            if len(res) < k:
                res.append(x)
            
        return res
