from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge for October 3rd, 2020.
    '''
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        Returns the number of unique k-diff pairs in an array. A k-diff pair
        is an integer pair such that nums[i] - nums[j] = k, given that i != j.
        
        Params:
            nums - A list of integers.
            
            k - The target difference of integer pairs.
            
        Returns:
            int - The unique number of k-diff integer pairs.
            
        Examples:
            findPairs([3,1,4,1,5], 2)             ->   2
            fingPairs([1,2,3,4,5], 1)             ->   4
            findPairs([1,3,1,5,4], 0)             ->   1
            findPairs([1,2,4,4,3,3,0,9,2,3], 3)   ->   2
            fingPairs([-1,-2,-3], 1)              ->   2
        '''
        nums_dict = {}
        for x in nums:
            nums_dict[x] = nums_dict.get(x, 0) + 1
            
        res = 0
        for b in nums_dict:
            a = b - k
            if a in nums_dict:
                if a == b and nums_dict[b] > 1:
                    nums_dict[b] = 1
                    res += 1
                elif a != b:
                    res += 1
                    
        return res
