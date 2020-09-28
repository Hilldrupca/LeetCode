from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge for September 28th, 2020.
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Returns the number of contiguous subarrays where the product of all
        elements is less than k.
        
        Params:
            nums - A list of integers.
            
            k - The number contiguous products must be less than.
            
        Returns:
            int - The count of subarray products less than k.
            
        Examples:
            numSubarrayProductLessThanK([10,5,2,6], 100)   ->   8
            numSubarrayProductLessThanK([1,1,1], 1)        ->   0
            numSubarrayProductLessThanK([2,3,4], 0)        ->   0
        '''
        if not nums or not k:
            return 0
        
        left_idx = idx = less_than_k = 0
        prod = 1
        for num in nums:
            prod *= num
            idx += 1
            while prod >= k and left_idx < idx:
                # Add the number of contiguous subarray products that
                # nums[left_idx] is part of. This is the same as
                # adding len(nums[left_idx:idx]).
                less_than_k += idx - left_idx - 1
                
                # Remove num[left_idx]'s contribution to current product
                prod /= nums[left_idx]
                
                left_idx += 1
        
        # Add remaining contiguous product counts
        less_than_k += (idx - left_idx) * (idx - left_idx + 1) // 2
        
        return less_than_k
