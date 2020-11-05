from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 5th, 2020.
    '''
    def minCostToMoveChips(self, position: List[int]) -> int:
        '''
        Given the positions of a number of chips, returns the minimum cost to
        move all chips to the same position when the following moves and costs
        apply:
        
            position[i] + or - 2 has a cost of 0
            position[i] + or - 1 has a cost of 1
            
        Params:
            position - A list of integers where each element represents the
                       position of a chip.
                       
        Returns:
            int - The minimum cost to move all chips to the same position.
            
        Examples:
            minCostToMoveChips([1,2,3])          ->   1
            minCostToMoveChips([2,2,2,3,3])      ->   2
            minCostToMoveChips([1,1000000000])   ->   1
            minCostToMoveChips([1])              ->   0
        '''
        even = odd = 0
        for x in position:
            if x%2:
                odd += 1
            else:
                even += 1
                
        return min(even, odd)
