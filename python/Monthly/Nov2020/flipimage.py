from typing import List

class Solution:
    '''
    LeetCode Monthly Challege problem for November 10th, 2020.
    '''
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        '''
        Given a binary matrix, returns a copy that is flipped horizontally, and
        inverted.
        
        Params:
            A - A list of binary lists. For example, [[0,1,0],[1,0,1]].
            
        Returns:
            List[List[int]] - A copy of the matrix flipped horizontally, and
                              inverted.
                              
        Example:
            flipAndInvertImage([[1,1,0],             [[1,0,0],
                                [1,0,1],         ->   [0,1,0],
                                [0,0,0]])             [1,1,1]]
        '''
        res = []
        for row in A:
            temp = []
            for e in row[::-1]:
                temp.append(0) if e else temp.append(1)
                
            res.append(temp)
            
        return res
