from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Starting from nums[0], returns whether or not you can reach the end of
        nums where each value represents how many spaces you can jump from that
        index.
        
        Params:
            nums - A list of integers. Each value represents how many indices
                   you can jump forward from that index.
                   
        Returns:
            bool - Whether or no you can reach the end.
            
        Examples:
            canJump([2,3,1,1,4])   ->   True
            canJump([3,2,1,0,4])   ->   False
            canJump([0])           ->   True
        '''
        steps = 0
        for x in range(len(nums)):
            steps = max(steps-1, nums[x])
            
            if steps >= len(nums)-1:
                return True
            
            if x < len(nums)-1 and steps == 0:
                return False
            
        return True
