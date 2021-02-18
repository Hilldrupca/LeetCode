from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Given a non-empty array of integers, every element appears
        twice except for one. Find that single one.
        
        Params:
            nums - List of integers where all but one integer
                   appears twice. The different integer should only
                   appear once.
        Returns:
            int - the integer who only appears once in nums.
        '''
        num_set = set()
        
        for x in nums:
            if x in num_set:
                num_set.remove(x)
            else:
                num_set.add(x)
                
        # Only one number should remain
        
        # If not, whatever number pop() returns will
        # have only appeared once
        return num_set.pop()
