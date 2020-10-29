from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 29th, 2020.
    '''
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        Returns the maxiumum distance to the closes person given a list of
        seats. A 1 represents a person in a seat, and 0 represents an empty
        seat.
        
        Constraints:
            2 <= len(seats) <= 2 * 10**4
            seats[i] is 0 or 1
            At least 1 empty seat
            At least 1 occupied seat
            
        Params:
            seats - A list of 0's and 1's. A 1 means the seat is occupied, and
                    a 0 means the seat is empty.
                    
        Returns:
            int - The maximum distance to the closest person.
            
        Examples:
            maxDistToClosest([1,0,0,0,1,0,1])   ->   2
            maxDistToClosest([1,0,0,0])         ->   3
            maxDistToClosest([0,1])             ->   1            
        '''
        seat_dist = 0
        cur = None
        for i in range(len(seats)):
            if seats[i]:
                if cur is None:
                    seat_dist = i
                else:
                    seat_dist = max(seat_dist, (i-cur)//2)
                
                cur = i
                    
        if not seats[-1]:
            seat_dist = max(seat_dist, len(seats) - 1 - cur)
            
        return seat_dist
