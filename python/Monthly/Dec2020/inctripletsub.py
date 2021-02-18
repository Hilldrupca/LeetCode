from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 18th, 2020.
    '''
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        Returns whether there exists a triplet of indices such that i < j < k,
        and nums[i] < nums[j] < nums[k].
        
        Constraints:
            1 <= len(nums) <= 10**5
            -2**31 <= nums[i] <= 2**31 - 1
            
        Params:
            nums - A list of integers.
            
        Returns:
            bool - Whether the given list contains a increasing triplet
                   subsequence.
                   
        Examples:
            increasingTriplet([1,2,3,4,5])     ->   True
            increasingTriplet([5,4,3,2,1])     ->   False
            increasingTriplet([2,1,5,0,4,6])   ->   True
            increasingTriplet([1,1,1])         ->   False
        '''        
        one = two = float('inf')
        
        for x in nums:
            if x < one:
                one = x
            elif one < x < two:
                two = x
            elif two < x:
                return True
            
        return False
