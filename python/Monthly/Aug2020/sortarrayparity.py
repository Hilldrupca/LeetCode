from typing import List

class Solution():
    '''
    LeetCode Monthly Challenge problem for August 21st, 2020.
    '''
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        '''
        Given an array A of non-negative integers, return an array consisting
        of all the even elements of A, followed by all the odd elements of A.

        You may return any answer array that satisfies this condition.
        
        Params:
            A - list of integers.
            
        Returns:
            list - a list of integers sorted with even numbers first, followed
                    by odd numbers.
        '''
        
        # Return sorted list based on modulo of 2
        return sorted(A, key= lambda x: x%2)
