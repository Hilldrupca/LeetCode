from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 16th, 2020.
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Searches a 2d matrix for the target value. Returns True if the value is
        in the matrix.
        
        Given:
            - Integers in each row are sorted in ascending order.
            - The first integer of each row is greater then the last integer of
              the previous row.
              
        Params:
            matrix - A list of integer lists.
            
            target - The integer to search for.
            
        Returns:
            bool - Whether or not the matrix contains the target value.
            
        Examples:
            Given the following matrices, m:
                [[ 1, 3, 5, 7],
                 [10,11,16,20],
                 [23,30,34,50]]
            
            searchMatrix(m, 3)    ->   True
            searchMatrix(m, 13)   ->   False
        '''
        if not matrix or not matrix[0]:
            return False
        
        for row in matrix:
            
            if row[0] <= target <= row[-1]:
                # Perform binary search of row
                low, high = 0, len(row)
                
                while low <= high:
                    
                    mid = (low + high)//2
                    
                    if row[mid] == target:
                        return True
                    
                    elif row[mid] < target:
                        low = mid + 1
                        
                    else:
                        high = mid - 1
                        
        return False
