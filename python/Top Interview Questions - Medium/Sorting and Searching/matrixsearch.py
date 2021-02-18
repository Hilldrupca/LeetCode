from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Given a 2d matrix whose rows and columns are in ascending order,
        returns whether or not it contains a target value.
        
        Params:
            matrix - A list of integer lists. Each row and column is in
                     ascending order.
                     
            target - The target value to look for.
            
        Returns:
            bools - If the matrix contains the target value.
            
        Examples:
            Given the following matrix, m:
                [[1,   4,  7, 11, 15],
                 [2,   5,  8, 12, 19],
                 [3,   6,  9, 16, 22],
                 [10, 13, 14, 17, 24],
                 [18, 21, 23, 26, 30]]
                 
            searchMatrix(m, 5)    ->   True
            searchMatrix(m, 20)   ->   False
        '''
        if not matrix or not matrix[0]:
            return False
                   
        for row in matrix:
            if row[0] > target:
                break
                
            # Perform binary search on row
            low, high = 0, len(row)-1
            while low <= high:
                mid = (high + low)//2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    
        return False
