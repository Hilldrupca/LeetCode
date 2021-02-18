from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 7th, 2020.
    '''
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        Returns an n x n 2d list populated with 1 to n^2 in spiral order. If
        n = 3, the following would be produced:
        
            [[1,2,3],
             [8,9,4],
             [7,6,5]]
        
        Params:
            n - An integer dimension for the square matrix.
            
        Returns:
            List[List[int]] - The 2d list in spiral order.
            
        Examples:
            generateMatrix(2)   ->   [[1,2],[4,3]]
            generateMatrix(3)   ->   [[1,2,3],[8,9,4],[7,6,5]]
        '''
        if n < 1:
            return []
        
        res = [[0]*n for _ in range(n)]
        r_min = c_min = x = 0
        r_max = c_max = n - 1
        
        while x < n*n:
            
            # traverse left to right
            for c in range(c_min, c_max+1):
                x += 1
                res[r_min][c] = x
                
            r_min += 1
            
            # traverse top to bottom
            for r in range(r_min, r_max+1):
                x += 1
                res[r][c_max] = x
                
            c_max -= 1
            
            # traverse right to left
            for c in range(c_max, c_min-1, -1):
                x += 1
                res[r_max][c] = x
                
            r_max -= 1
            
            # traverse bottom to top
            for r in range(r_max, r_min-1, -1):
                x += 1
                res[r][c_min] = x
                
            c_min += 1
            
        return res
