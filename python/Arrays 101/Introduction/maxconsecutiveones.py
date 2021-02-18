from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        Given a binary list, returns the maximum number of consecutve ones.
        
        Params:
            nums - A list of 1's and 0's.
            
        Returns:
            int - Maximum number of consecutive ones.
            
        Examples:
            findMaxConsecutiveOnes([1,1,0,1,1,1])   ->   3
            findMaxConsecutiveOnes([1,0,1,1,0,1])   ->   2
        '''
        max_ones = 0
        count = 0
        for x in nums:
            if x:
                count += 1
            else:
                max_ones = max(max_ones, count)
                count = 0
                
        return max(max_ones, count)
