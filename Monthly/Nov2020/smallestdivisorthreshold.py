from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 6th, 2020.
    '''
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        Given a list of integers and a threshold, returns the smallest positive
        divisor such that the sum of all divisions of the lists elements is
        less than or equal to threshold.
        
        Each division is rounded up. For example: 7/3 = 3, and 10/2 = 5.
        
        Params:
            nums - A list of positive integers.
            
            threshold - An integer threshold.
            
        Returns:
            int - A positive divisor.
            
        Examples:
            smallestDivisor([1,2,5,9], 6)       ->   5
            smallestDivisor([2,3,5,7,11], 11)   ->   3
            smallestDivisor([19], 5)            ->   4
            smallestDivisor([22,22,22,22], 4)   ->   22
        '''
        # Narrow possible divisors using binary search
        l, r = 1, max(max(nums), threshold)
        while l < r:
            mid = (l+r)//2
            total = 0
            for x in nums:
                total += -(-x//mid) # same as math.ceil
            
            if  total > threshold:
                l = mid + 1
            else:
                r = mid

        return l
