from collections import deque
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 13th, 2021.
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        Given an N x N binary matrix, returns the length of the shortest path
        from the top left (0,0) cell to the bottom right cell (N-1, N-1). Cells
        with a value of 1 are considered to be impassable, and cells with a
        value of 0 are considered open paths. For each cell, travel is allowed
        to the up to eight directionally connected cells.
        
        Constraints:
            1 <= len(grid) == len(grid[0]) <= 100
            grid[r][c] is 0 or 1
            
        Params:
            grid - A binary matrix.
            
        Returns:
            int - Length of shorted path from top left cell to bottom right
                  cell. -1 if no such path exists.
                  
        Examples:
            shortestPathBinaryMatrix([[0,1],
                                      [1,0]])     ->   2
                                     
            shortestPathBinaryMatrix([[0,0,0],
                                      [1,1,0],
                                      [1,1,0]])   ->   4
                                      
            shortestPathBinaryMatrix([[1,0,0],
                                      [1,1,0],
                                      [1,1,0]])   ->   -1
        '''
        m = len(grid)
        
        unseen = set()
        
        for y in range(m):
            for x in range(m):
                if not grid[y][x]:
                    unseen.add((y,x))
                    
        if (0,0) not in unseen:
            return -1
        
        unseen.remove((0,0))
        queue = deque([((0,0), 1)])
        
        while queue:
            (y, x), s = queue.popleft()
            
            if y == x == m - 1:
                return s
            
            y_min, y_max = max(0, y-1), min(m, y+2)
            x_min, x_max = max(0, x-1), min(m, x+2)
            
            for n_y in range(y_min, y_max):
                for n_x in range(x_min, x_max):
                    cell = (n_y, n_x)
                    
                    if cell in unseen:
                        queue.append((cell, s+1))
                        unseen.remove(cell)
                        
        return -1
