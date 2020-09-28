from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        Returns whether an array of integers contains an increasing
        subsequence of length 3.
        
        Formally:
            arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1
            
        Examples:
            increasingTriplet([1,2,3,4,5])     ->   True
            increasingTriplet([5,4,3,2,1])     ->   False
            increasingTriplet([2,1,5,0,4,6])   ->   True
        '''
        low = mid = float('inf')
        for x in nums:
            if x <= low:
                low = x
            elif x <= mid:
                mid = x
            else:
                return True
            
        return False
