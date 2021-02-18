from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        Replaces each element with the greatest element to its right, and
        replaces the last element with -1. Then returns the list.
        
        Params:
            arr - A list of integers.
            
        Returns:
            List[int] - The list with elements replaced by greatest right
                        element, and last element = -1.
                        
        Example:
            replaceElements([17,18,5,4,6,1])   ->   [18,6,6,6,1,-1]
            replaceElements([1])               ->   [-1]
            replaceElements([])                ->   []
        '''
        max_right = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i], max_right = max_right, max(max_right, arr[i])
            
        return arr
