from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 25th,2020.
    '''
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Returns all elements of a given M x N matrix in diagonal order.
        
        Disclosure:
            Solution primarily comes from the following link:
            https://www.geeksforgeeks.org/print-matrix-diagonal-pattern/?ref=rp
            
            I made a few changes such as removing the isUp flag, and adding
            checks for the given matrix.            
        
        Constraints:
            Total number of elements <= 10**4
            
        Params:
            matrix - A list of integer lists.
            
        Returns:
            List[int] - The elements of matrix in diagonal order.
            
        Examples:
            matrix = [[1,2,3],[4,5,6],[7,8,9]]
            findDiagonalOrder(matrix)   ->   [1,2,4,7,5,3,6,8,9]
            
            matrix = [[1,2],[3,4],[5,6]]
            findDiagonalOrder(matrix)   ->   [1,2,3,5,4,6]
            
            findDiagonalOrder([])       ->   []
        '''
        if not matrix or not matrix[0]:
            return []        
        
        m, n = len(matrix), len(matrix[0])
        i = j = k = 0
        res = []
        while k < m * n:
            # Traverse up and to the right
            while i >= 0 and j < n:
                res.append(matrix[i][j])
                i, j, k = i - 1, j + 1, k + 1
                
            if i < 0 and j <= n - 1:
                i = 0
            elif j == n:
                i += 2
                j -= 1
            
            # Traverse down and to the left
            while j >= 0 and i < m:
                res.append(matrix[i][j])
                i, j, k = i + 1, j - 1, k + 1
            
            if j < 0 and i <= m - 1:
                j = 0
            elif i ==  m:
                j += 2
                i -= 1
            
        return res
