from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        In-place 90 degree rotation of a given n x n list of lists.
        
        Params:
            matrix - A list of lists containing integers.
            
        Returns:
            None - In-place rotation of matrix.
            
        Examples:
            [[1,2,3],       [[7,4,1],
             [4,5,6],   ->   [8,5,2],
             [7,8,9]]        [9,6,3]]
             
             
            [[ 5, 1, 9,11],       [[15,13, 2, 5]
             [ 2, 4, 8,10],        [14, 3, 4, 1]
             [13, 3, 6, 7],   ->   [12, 6, 8, 9],
             [15,14,12,16]]        [16, 7,10,11]]
        '''
        idx = 0
        for row in zip(*matrix[::-1]):
            matrix[idx] = list(row)
            idx += 1
