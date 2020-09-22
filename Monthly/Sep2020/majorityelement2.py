from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 22nd, 2020.
    '''
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        Finds all elements in nums that appear more than len(nums)/3 times.
        
        Params:
            nums - List of integers.
            
        Returns:
            List[int] - A list of integers who appear more than len(nums)/3
                        times.
        
        Examples:
            majorityElement([3,2,3])             ->   [3]
            majorityElement([1,1,1,3,3,2,2,2])   ->   [1,2]
        '''        
        occurances = {}
        for x in nums:
            occurances[x] = occurances.get(x, 0) + 1
        
        res = []
        for x,y in occurances.items():
            if y > len(nums)/3:
                res.append(x)
                
        return res
