from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 18th, 2021.
    '''
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        Given a list of integers and a target sum, returns the number of pairs
        whose sum equals k. Each number is only used in one pair.
        
        Constraints:
            1 <= len(nums) <= 10**5
            1 <= nums[i] <= 10**9
            1 <= k <= 10**9
            
        Params:
            nums - A list of integers.
            
            k - Target integer sum.
            
        Returns:
            int - Number of k sum pairs.
            
        Examples:
            maxOperations([1,2,3,4], 5)     ->   2
            maxOperations([3,1,3,4,3], 6)   ->   1
        '''
        counts, pairs = {}, 0
        get = counts.get
        
        for x in nums:
            diff = k - x
            
            if get(diff, 0):
                pairs += 1
                counts[diff] -= 1
            else:
                counts[x] = get(x, 0) + 1
                
        return pairs
