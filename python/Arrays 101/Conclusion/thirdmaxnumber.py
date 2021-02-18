from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        Given a list of integers, returns the third largest unique number (or
        largest if there is no third largest) in O(n) time.
        
        Params:
            nums - A list of integers.
            
        Returns:
            int - The third largest number, or the largest if there is no third
                  largest. Returns negative infinity if given an empty list.
                  
        Examples:
            thirdMax([3,2,1])     ->   1
            thirdMax([1,2])       ->   2
            thirdMax([2,2,3,1])   ->   1
            thirdMax([])          ->   -inf
        '''
        one = two = three = float('-inf')
        for x in nums:
            if x > one:
                one, two, three = x, one, two
            elif one > x > two:
                two, three = x, two
            elif two > x > three:
                three = x
                
        return three if three != float('-inf') else one
