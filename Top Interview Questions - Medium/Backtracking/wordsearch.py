from typing import List
from collections import Counter
from itertools import chain

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Returns whether or not a given word is present within board of letters.
        A word is constructed by checking horizontal and vertically adjacent
        spaces.
        
        Params:
            board - A list of lists of letters. Letters can be either uppercase
                    or lowercase.
                    
            word - The word to find within the board. Checks are case sensitive.
            
        Returns:
            bool - Whether word is present in the board.
            
        Examples:
            Given the following board (b):
            
                [['A','B','C','E'],
                 ['S','F','C','S'],
                 ['A','D','E','E']]
                 
            exist(b, 'ABCCED')   ->   True
            exist(b, 'SEE')      ->   True
            exist(b, 'see')      ->   False
            exist(b, 'ABCB')     ->   False
            
        '''
        if not board or not word:
            return False
        
        '''
        I did not come up with the use of Counters. Run time already beat ~97%
        of submissions. The follow code snippet improved runtime from ~260ms
        to ~140ms over 89 tests. Code now reliably beats ~%100 of submissions.
        '''
        board_counter = Counter(chain(*board))
        word_counter = Counter(word)
        if any(c>board_counter[w] for w,c in word_counter.items()):
            return False
        
        height = len(board) - 1
        width = len(board[0]) - 1     
        self.present = False
        
        # A depth first search of adjacent spaces
        def helper(y, x, i):
            if self.present:
                return
            
            if i == len(word) - 1:
                self.present = True
                return
            
            # Mark visited spaces
            board[y][x] = board[y][x].lower() if board[y][x].isupper() \
                                              else board[y][x].upper()
            
            if y > 0 and board[y-1][x] == word[i+1]:
                helper(y-1, x, i+1)
            if y < height and board[y+1][x] == word[i+1]:
                helper(y+1, x, i+1)
            if x > 0 and board[y][x-1] == word[i+1]:
                helper(y, x-1, i+1)
            if x < width and board[y][x+1] == word[i+1]:
                helper(y, x+1, i+1)
            
            # Restore space to previous state
            board[y][x] = board[y][x].lower() if board[y][x].isupper() \
                                              else board[y][x].upper()
        
        # Loop over board to find spaces with first letter of word
        for y in range(height+1):
            for x in range(width+1):
                if board[y][x] == word[0]:
                    helper(y, x, 0)
                    if self.present:
                        return self.present
                    
        return self.present
