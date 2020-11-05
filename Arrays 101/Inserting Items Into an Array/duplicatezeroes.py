from typing import List

class Solution:
    def duplicateZeroes(self, arr: List[int]) -> None:
        '''
        In-place duplication of zeroes in a list of integers. At each zero
        element, remaining elements are shifted right to make room for new
        zero.
        
        Elements beyond the original length of the list are deleted.
        
        Params:
            arr - A list of integers.
            
        Returns:
            None - In-place duplication of zeroes.
            
        Examples:
            arr = [1,0,2,3,0,4,5,0]
            duplicateZeroes(arr)   ->   arr == [1,0,0,2,3,0,0,4]
            
            arr = [1,2,3]
            duplicateZeroes(arr)   ->   arr == [1,2,3]
            
            arr = [0,0,0]
            duplicateZeroes(arr)   ->   arr == [0,0,0]
        '''
        i = 0
        while i < len(arr):
            if not arr[i]:
                del arr[-1]
                arr.insert(i, 0)
                i += 2
            else:
                i += 1
