from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 25th, 2021.
    '''
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        '''
        Checks if a list containing only 1's and 0's has all 1's k places
        apart from each other.
        
        Constraints:
            1 <= len(nums) <= 10**5
            0 <= k <= len(nums)
            nums[i] is 0 or 1
            
        Params:
            nums - A binary list.
            
            k - Required distance between 1's.
            
        Returns;
            bool - If all ones are k places apart.
            
        Examples:
            kLengthApart([1,0,0,0,1,0,0,1], 2)   ->   True
            kLengthApart([1,0,0,1,0,1], 2)       ->   False
            kLengthApart([1,1,1,1,1], 0)         ->   True
            kLengthApart([0,1,0,1], 1)           ->   True
        '''
        spaces = float('inf')
        for x in nums:
            if x and spaces > k:
                spaces = 0
            elif x:
                return False
            
            spaces += 1
            
        return True
