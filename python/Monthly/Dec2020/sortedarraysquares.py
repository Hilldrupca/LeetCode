from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 15th, 2020.
    '''
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Given a list of integers, returns the squares in non-decreasing order.
        
        Constraints:
            1 <= len(nums) <= 10**4
            -10**4 <= nums[i] <= 10**4
            nums is sorted in non-decreasing order
            
        Params:
            nums - A list of integers.
            
        Returns:
            List[int] - A list of squares sorted in non-decreasing order.
            
        Examples:
            sortedSquares([-4,-1,0,3,10])   ->   [0,1,9,16,100]
            sortedSquares([-7,-3,2,3,11])   ->   [0,9,9,49,121]
        '''
        return sorted(x*x for x in nums)
