from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Returns the number of islands in a given list of list of '1's and '0's.
        A '1' represents land while a '0' represents water. An island is any
        number of '1's connected vertically and horizontally. Grid spaces
        that would be out of bounds are considered water.
        
        Params:
            grid - A list of lists containing '1's and '0's.
                      - '1' represents land
                      - '0' represents water
        
        Returns:
            int - The number of islands contained in the grid.
        
        Examples:
            Given the following map:
            
                [['1','1','0','0','0'],
                 ['1','1','0','0','0'],
                 ['0','0','1','0','0'],
                 ['0','0','0','1','1']]
                 
            numIslands() returns 3
            
            
            Given the following map:
            
                [["0","1","0"],
                 ["1","0","1"],
                 ["0","1","0"]]
                 
            numIslands() returns 4
        '''
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # discover and mark current island
                if grid[row][col] == '1':
                    self._dfs(row, col, grid)
                    islands += 1
                    
                # reset to original value
                if grid[row][col] == '00':
                    grid[row][col] = '1'
                    
        return islands
    
    def _dfs(self, row: int, col: int, grid: List[List[int]]) -> None:
        '''
        Helper method for numIslands() - marks already visited 'land' and
        discovers neighboring 'land'.
        '''
        grid[row][col] = '00'
        
        if row < len(grid) - 1 and grid[row+1][col] == '1':
            self._dfs(row+1, col, grid)
        
        if row > 0 and grid[row-1][col] == '1':
            self._dfs(row-1, col, grid)
            
        if col < len(grid[0]) - 1 and grid[row][col+1] == '1':
            self._dfs(row, col+1, grid)
            
        if col > 0 and grid[row][col-1] == '1':
            self._dfs(row, col-1, grid)
