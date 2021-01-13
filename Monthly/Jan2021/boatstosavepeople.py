from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 13th, 2021.
    '''
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Given a list of peoples' weights and the maximum weight limit of a
        boat, returns the minimum boats needed to save every person. Each boat
        can carry at most 2 people.
        
        Constraints:
            1 <= len(people) <= 50000
            1 <= people[i] <= limit <= 30000
            
        Params:
            people - A list of integers. (Peoples' weights)
            
            limit - The weight limit of each boat.
            
        Returns:
            int - The minimum number of boats to rescue everyone.
            
        Examples:
            numRescueBoats([1,2], 3)       ->   1
            numRescueBoats([3,2,2,1], 3)   ->   3
            numRescueBoats([3,5,3,4], 5)   ->   4
        '''
        people = sorted(people)
        l, r = 0, len(people)-1
        boats = 0
        
        while l <= r:
            
            if people[l] + people[r] <= limit:
                l += 1
                
            r -= 1
            boats += 1
            
        return boats
