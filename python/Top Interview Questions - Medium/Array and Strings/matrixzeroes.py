from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        In-place zeroing of respective row and column if an elemnent is zero.
        
        Params:
            matrix - A list of lists of integers.
            
        Example:
            Given the following matrix:
            
            matrix = [[1,1,1],
                      [1,0,1],
                      [1,1,1]]
                      
            After setZeroes(matrix) it would become:
            
                [[1,0,1],
                 [0,0,0],
                 [1,0,1]]
        '''
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    if matrix[y][0] =='c':
                        matrix[y][0] = 'rc'
                    elif matrix[y][0] != 'rc':
                        matrix[y][0] = 'r'
                        
                    if matrix[0][x] == 'r':
                        matrix[0][x] = 'rc'
                    elif matrix[0][x] != 'rc':
                        matrix[0][x] = 'c' 
                        
                    
        for y in range(len(matrix)-1,-1,-1):
            if matrix[y][0] in ['r', 'rc']:
                for x in range(len(matrix[y])):
                    matrix[y][x] = 0                  
            else:
                for x in range(len(matrix[y])):
                    if matrix[0][x] in ['c','rc']:
                        matrix[y][x] = 0
