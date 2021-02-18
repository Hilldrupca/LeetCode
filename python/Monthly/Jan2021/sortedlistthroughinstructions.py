from typing import List
from sortedcontainers import SortedList

class Solution();
    '''
    LeetCode Monthly Challenge problem for January 10th, 2021.
    
    NOTE: No accompanying test file. This solution makes use of the
          sortedcontainers module, which can be installed via pip:
        
              pip install sortedcontainers
    '''
    def createSortedArray(self, instructions: List[int]) -> int:
        '''
        Given an integer array instructions, you are asked to create a sorted
        array from the elements in instructions. You start with an empty
        container nums. For each element from left to right in instructions,
        insert it into nums. The cost of each insertion is the minimum of the
        following:

            - The number of elements currently in nums that are strictly less
              than instructions[i].
            - The number of elements currently in nums that are strictly
              greater than instructions[i].

        Return the total cost to insert all elements from instructions into
        nums. Since the answer may be large, return it modulo 10**9 + 7
        
        Constraints:
            1 <= len(instructions) <= 10**5
            1 <= instructions[i] <= 10**5
        
        Params:
            instructions - A list of integers.
            
        Returns:
            int - The modulo 10**9 + 7 of the total cost to insert all
                  elements.
        
        Examples:
            createSortedArray([1,5,6,2])             ->   1
            createSortedArray([1,2,3,6,5,4])         ->   3
            createSortedArray([1,3,3,3,2,4,2,1,2])   ->   4
        '''
        cost, arr = 0, SortedList()
        for n in instructions:
            left, right = arr.bisect_left(n), arr.bisect_right(n)
            cost += min(left, len(arr) - right)
            
            arr.add(n)
            
        return cost % (10**9 + 7)
