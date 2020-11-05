from typing import List

class Solution:
    def checkIfExists(self, arr: List[int]) -> bool:
        '''
        Given a list of integers, check if there exists two integers N and M
        such that N is the double of M. Note the numbers must has different
        indices.
        
        Params:
            arr - A list of integers.
            
        Returns:
            bool - Whether a list of integers contains the double of an
                   element.
                   
        Examples:
            checkIfExists([10,2,5,3])              ->   True
            checkIfExists([7,1,14,11])             ->   True
            checkIfExists([3,1,7,11])              ->   False
            checkIfExists([[-2,0,10,-19,4,6,-8])   ->   False
        '''
        nums = set()
        for x in arr:
            if x/2 in nums or x*2 in nums:
                return True
            
            nums.add(x)
            
        return False
