from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 1st, 2021.
    '''
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        '''
        Given a list of distince integers (arr), and a list of distinct integer
        lists (pieces), returns if arr can be made by concatenating the lists
        in pieces. Concatentation can be done in any order, but the integers in
        pieces[i] cannot be rearranged.
        
        Constraints:
            1 <= len(pieces) <= len(arr) <= 100
            sum(len(pieces[i])) == len(arr)
            1 <= len(pieces[i]) <= len(arr)
            1 <= arr[i], pieces[i][j] <= 100
            The integers in arr are distinct
            All integers in pieces are distinct
            
        Params:
            arr - A list of distinct integers.
            
            pieces - A list of integers lists. Each integer must be distinct.
            
        Returns:
            bool - If arr can be made by concatenating lists in pieces.
            
        Examples:
            canFormArray([85],[[85]])                        ->   True
            canFormArray([85,1,2], [[85,2,1]])               ->   False
            canFormArray([15,88], [[88],[15])                ->   True
            canFormArray([49,18,16], [[16,18,49]])           ->   False
            canFormArray([91,4,64,78], [[78],[4,64],[91]])   ->   True
        '''
        starts_with = {p[0]:p for p in pieces}
            
        i = 0
        while i < len(arr) and arr[i] in starts_with:
            
            p = starts_with.pop(arr[i])
            if arr[i:i+len(p)] == p:
                i += len(p)
            
        return i == len(arr)
