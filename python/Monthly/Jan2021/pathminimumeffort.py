from heapq import heappop, heappush
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 26th, 2021.
    '''
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        Given a 2d list of heights, returns the minimum effort from the top
        left cell to the bottom right cell. A route's effort is the maximum
        absolute differefence in heights between two consecutive cells.
        Possible moves from each cell can either be up, down, left, or right.
        
        Constraints:
            rows == len(heights)
            columns == len(heights[0])
            1 <= rows, columns <= 100
            1 <= heights[i][j] <= 10**6
            
        Params:
            heights - A list of positive integer lists.
            
        Returns:
            int - The minimum effort from the top left to the bottom right
                  cell.
                  
        Examples:
            Given the following matrix, a:
            
                    [[1,2,2],
                     [3,8,2],
                     [5,3,5]]
            
            minimumEffortPath(a)   ->   2
            
            Given the following matrix, b:
            
                    [[1,2,3],
                     [3,8,4],
                     [5,3,5]]
                     
            minimumEffortPath(b)   ->   1
            
            Given the following matrix, c:
            
                    [[1,2,1,1,1],
                     [1,2,1,2,1],
                     [1,2,1,2,1],
                     [1,2,1,2,1],
                     [1,1,1,2,1]]
                     
            minimumEffortPath(c)   ->   0
        '''
        row, col = len(heights), len(heights[0])
        graph = {(r, c): float('inf') for r in range(row) for c in range(col)}
        graph[(0,0)] = 0
        pq = [(0,0,0)]
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while pq:
            h, r, c = heappop(pq)
            
            if r == row - 1 and c == col - 1:
                return h
            
            for y,x in moves:
                n_r, n_c = r + y, c + x
                coord = (n_r,n_c)
                if coord in graph:
                    diff = max(h, abs(heights[r][c] - heights[n_r][n_c]))
                    if diff < graph[coord]:
                        graph[coord] = diff
                        heappush(pq, (diff, n_r, n_c))
                        
        return 0
