
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Returns the number of unique paths in an m x n grid from the top-left
        corner to the bottom-right corner.
        
        Params:
            m - The number of rows.
            
            n - The number of columns.
            
        Returns:
            int - The number of unique paths.
            
        Examples:
            uniquePaths(3,7)   ->   28
            uniquePaths(3,2)   ->   3
            uniquePaths(7,3)   ->   28
            uniquePaths(3,3)   ->   6
        '''
        if not m or not n:
            return 0
        
        grid = [[0 for x in range(n)] for y in range(m)]
        
        for y in range(m):
            for x in range(n):
                if not y or not x:
                    grid[y][x] = 1
                else:
                    grid[y][x] = grid[y-1][x] + grid[y][x-1]
                    
        return grid[m-1][n-1]
