from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 30th, 2020.
    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        '''
        Background reading: John Horton Conway's Game of Life.
        
        Given an M x N grid of cells, modifies the board in-place to the next
        state. A live cell is represented by 1, and a dead cell is prepresented
        by a 0. A cell's next state is determined by the following rules:
        
            Any live cell with fewer than two live neighbors dies
            Any live cell with two or three live neighbors lives
            Any live cell with more than three live neighbors dies
            Any dead cell with exactly three live neighbors becomes a live cell
            
        Constraints:
            m == len(board)
            n == len(board[i])
            1 <= m, n <= 25
            board[i][j] is 0 or 1
            
        Params:
            board - A list of binary lists.
            
        Returns:
            None - Board is modified in-place to the next state.
            
        Examples:
            Below are examples of boards and their next state:
            
            [[0,1,0],              [[0,0,0],
             [0,0,1],       ->      [1,0,1],
             [1,1,1],               [0,1,1],
             [0,0,0]]               [0,1,0]]
             
             
            [[1,1],                [[1,1],
             [1,0]]         ->      [1,1]]
        '''
        if not len(board) or not len(board[0]):
            return
        
        for row in board:
            if len(row) != len(board[0]):
                return
        
        m = len(board)
        n = len(board[0])
        
        # Visit each cell of board
        for row in range(m):
            for col in range(n):
                
                # check rightmost neighbor of current cell and
                # all neighbors below current cell
                for y, x in [(0,1),(1,-1),(1,0),(1,1)]:
                    if 0 <= col + x < n and row + y < m:
                        board[row][col] += 2 * (board[row+y][col+x] % 2)
                        board[row+y][col+x] += 2 * (board[row][col] % 2)
                    
                if 5 <= board[row][col] <= 7:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
