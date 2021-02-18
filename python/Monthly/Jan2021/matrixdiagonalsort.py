from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 23rd, 2021.
    '''
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        Given an M x N matrix, returns a copy with the diagonals sorted in
        ascending order.
        
        Constraints:
            1 <= len(mat), len(mat[0]) <= 100
            1 <= mat[i][j] <= 100
            
        Params;
            mat - An M x N matrix of positive integers.
            
        Returns:
            List[List[int]] - A copy of given matrix with diagonals sorted in
                              ascending order.
                              
        Example:
            Given the following matrix, mat:
            
                    [[3,3,1,1],
                     [2,2,1,2],
                     [1,1,1,2]]
            
            diagonalSort(mat) returns:
            
                    [[1,1,1,1],
                     [1,2,2,2],
                     [1,2,3,3]]
        '''
        m, n = len(mat), len(mat[0])
        
        res = [[0]*n for _ in range(m)]
        up, over = m-1, 0
        
        while up or over < n:
            temp = []
            y, x = up, over
            while y < m and x < n:
                temp.append(mat[y][x])
                y, x = y + 1, x + 1
                
            temp.sort()
            while y and x:
                y, x = y - 1, x - 1
                res[y][x] = temp.pop()
                
            if up:
                up -= 1
            else:
                over += 1
                
        return res
