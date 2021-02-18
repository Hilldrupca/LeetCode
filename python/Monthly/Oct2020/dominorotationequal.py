from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 19th, 2020.
    '''
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        '''
        Returns the minimum number of domino rotations to make either the top
        or bottom row equal to the same number. If it's not possible, returns
        -1.
        
        Params:
            A - A list of integers. (Top domino row)
            B - A list of integers. (Bottom domino row)
            
        Returns:
            int - The minimum rotations to make either top or bottom row all
                  the same. Returns -1 if not possible.
                  
        Example:
            minDominoRotations([2,1,2,4,2,2],
                               [5,2,6,2,3,2])   ->   2
                               
            minDominoRotations([3,5,1,2,3],
                               [3,6,3,3,4])     ->   -1
                               
            minDominoRotations([1,1,1,1,1],
                               [1,1,1,1,1])     ->   0
        '''
        if A == B:
            return 0

        top = {}
        bot = {}
        same = {}
        start = A[0], B[0]
        
        # Count num occurances in each row
        for i in range(len(A)):                
            if A[i] not in start and B[i] not in start:
                return -1            
            elif A[i] != B[i]:
                top[A[i]] = top.get(A[i], 0) + 1
                bot[B[i]] = bot.get(B[i], 0) + 1
            else:
                same[A[i]] = same.get(A[i], 0) + 1
        
        # Checks if either row is all one number
        if len(top.keys() | same.keys()) == 1 or len(bot.keys() | same.keys()) == 1:
            return 0
        
        # Finds which number is dominant, and min rotations
        for num in top.keys() & bot.keys():
            if top.get(num,0) + bot.get(num,0) + same.get(num,0) == len(A):
                return min(top.get(num), bot.get(num))
            
        return -1
