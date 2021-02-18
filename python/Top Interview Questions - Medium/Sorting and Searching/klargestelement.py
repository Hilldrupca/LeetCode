from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Returns the kth largest element in a given array.
        
        Assumption:
            1 <= k <= len(nums)
            
        Params:
            nums - A list of integers.
            
            k - Which rank from the largest to return.
            
        Returns;
            int - The kth largest element in nums.
            
        Examples:
            findKthLargest([3,2,1,5,6,4], 2)         ->   5
            findKthLargest([3,2,3,1,2,4,5,5,6], 4)   ->   4
        '''
        return sorted(nums, reverse=True)[k-1]
