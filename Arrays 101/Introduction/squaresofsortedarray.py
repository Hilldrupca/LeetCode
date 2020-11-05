from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        Gien a list of integers sorted in ascending order, returns a list of
        the squares of each number also sorted in ascending order.
        
        Params:
            A - A list of integers.
            
        Returns:
            List[int] - A list of squares sorted in ascending order.
            
        Examples:
            sortedSquares([-4,-1,0,3,10])   ->   [0,1,9,16,100]
            sortedSquares([-7,-3,2,3,11])   ->   [4,9,9,49,121]
        '''
        squares = [x*x for x in A]
        squares.sort()
        return squares
