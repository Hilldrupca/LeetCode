from typing import List

class Solution:
    def plusone(self, digits: List[int]) -> List[int]:
        '''
        Given a non-empty array of digits representing a non-negative integer,
        increment one to the integer.

        The digits are stored such that the most significant digit is at the
        head of the list, and each element in the array contains a single
        digit.

        You may assume the integer does not contain any leading zero, except
        the number 0 itself.
        
        Params:
            digits - list of integers representing a larger number
            
        Return:
            list - digits incremented by 1
            
        Examples:
            plusone([1,2,3]) -> [1,2,4]
            
            plusone([4,3,2,1]) -> [4,3,2,2]
            
            plusone([9,9]) -> [1,0,0]
        '''
        
        # Convert each item in digit to a str then concatenate
        num = ''.join([str(x) for x in digits])
        num = int(num) + 1
        
        # Convert each character back into an int
        return [int(x) for x in str(num)]
