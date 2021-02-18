from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 23rd, 2020.
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        Returns whether or not a list of integers contains a pattern such that
        nums[i] < num[j] < nums[k] where i < k < j.
        
        # Original implementation under current
        
        Params:
            nums - A list of integers.
            
        Returns:
            bool - Whether nums contains the 132 pattern.
            
        Examples:
            find132pattern([1,2,3,4])    ->   False
            find132pattern([3,1,4,2])    ->   True
            find132pattern([-1,3,2,0])   ->   True
            find132pattern([3,2])        ->   False
        '''
        stack = []
        _max = float('-inf')
        for num in nums[::-1]:
            if num < _max:
                return True
            while stack and stack[-1] < num:
                _max = stack.pop()
            stack.append(num)
        return False
    
    
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        from collections import Counter
        
        counts = Counter(nums)
        start = float('inf')
        for num in nums:            
            counts[num] -= 1
            if not counts[num]:
                counts.pop(num)
                
            start = min(start, num)
            if start != num:
                for mid in counts:
                    if start < mid < num:
                        return True
        
        return False
    '''
