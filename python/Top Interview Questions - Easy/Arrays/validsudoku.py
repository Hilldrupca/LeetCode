from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> bool:
        '''
        Determine if a Sudoku board is valid (not necessarily solvable). Only
        checks the starting numbers to make sure they doesn't appear twice in
        the same row, column, or 3x3 square.
        
        Params:
            board - A list of lists containing integers, and ".". 
            
        Returns:
            bool - Whether or not the board is valid.
        '''
        section = {'col': {}, 'row': {}, 'sqr': {}}
        
        for y in range(9):
            # Initialize row number set
            if y not in section['row']:
                section['row'][y] = set()
            
            sqr_y = y//3   # 3x3 square's y value
            
            for x in range(9):
                
                sqr_x = x//3   # 3x3 square's x value
                sqr = sqr_x, sqr_y
                tile = board[y][x]
                
                if tile == '.':
                    continue
                
                # Initialize column number set
                if x not in section['col']:
                    section['col'][x] = set()
                    
                # Initialize 3x3 square set
                if sqr not in section['sqr']:
                    section['sqr'][sqr] = set()
                
                # Check if tile has already appeared in current column or row
                if tile in section['row'][y] or tile in section['col'][x]:
                    return False
                
                # Add tile to current column and row
                section['col'][x].add(tile)
                section['row'][y].add(tile)
                
                # Check if tile has already appeared in current 3x3 square
                if tile in section['sqr'][sqr]:
                    return False
                
                # Add tile to current 3x3 square
                section['sqr'][sqr].add(tile)
                
        return True
                    
                
