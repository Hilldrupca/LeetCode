from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''
        Given a list of integers, returns how many elements are moved when
        sorting the list.
        
        Params:
            heights - A list of integers.
            
        Returns:
            int - Number of elements moved in order to sort.
            
        Examples:
            heightChecker([1,1,4,2,1,3])   ->   3
            heightChecker([5,1,2,3,4])     ->   5
            heightChecker([1,2,3,4,5])     ->   0
        '''
        temp = sorted(heights)
        diff = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                diff += 1
                
        return diff
