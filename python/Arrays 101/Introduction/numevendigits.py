from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        '''
        Given a list of integers, returns how many numbers have an even number
        of digits.
        
        Params:
            nums - A list of integers.
            
        Returns:
            int - How many numbers haven an even number of digits.
            
        Examples:
            findNumbers([12,345,2,6,7896])    ->   2
            findNumbers([555,901,482,1771])   ->   1
        '''
        nums_even_len = 0
        for x in nums:
            if not len(str(x))%2:
                nums_even_len += 1
                
        return nums_even_len
