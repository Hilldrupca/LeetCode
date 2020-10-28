from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 28th, 2020.
    '''
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        Given a sorted list of unique integers, returns the smallest sorted
        list of ranges that cover all numbers in the given list.
        
        Params:
            nums - A list of unique integers.
            
        Returns:
            List[str] - The smallest sorted list of ranges.
            
        Examples:
            summaryRanges([0,1,2,4,5,7])   -> ['0->2','4->5','7']
            summaryRanges([-1])            -> ['-1']
            summaryRanges([0])             -> ['0']
            summaryRanges([])              -> []
        '''
        if not nums:
            return []
        
        res = []
        start = end = nums[0]
        for x in nums:
            
            if x > end + 1:
                res.append(f"{start}{f'->{end}' if start != end else ''}")
                start = end = x
                
            else:
                end = x
                
        res.append(f"{start}{f'->{end}' if start != end else ''}")
        
        return res
