from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        Given a list of integers where 1 <= a[i] <= len(a), returns a list
        if integers that do not appear.
        
        Params:
            nums - A list of integers.
            
        Returns:
            List[int] - A list of the missing integers.
            
        Examples:
            findDisappearedNumbers([4,3,2,7,8,2,3,1])   ->   [5,6]
            findDisappearedNumbers([1,2,1])             ->   [3]
            findDisappearedNumbers([])                  ->   []
        '''
        poss = set(range(1,len(nums)+1))
        for x in nums:
            if x in poss:
                poss.remove(x)
                
        return list(poss)
