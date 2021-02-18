from typing import List
from heapq import heappush, heappop

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 21st, 2020.
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        Determine if it's possible to pick up and drop off all passengers
        for all given trips. Vehicle only drives east. No turning around.
        
        Params:
            trips - A list of lists with information about each trip.
                    i[0] = number of passengers
                    i[1] = pick up distance from start
                    i[2] = drop off distance from start
                    
            capacity - The maximum number of people the car can hold at once.
            
        Returns:
            bool - Whether or not all passenger can be picked up and
                   dropped off.
                   
        Examples:
            carPooling([[2,1,5],[3,3,7]], capacity=4)            ->   False
            carPooling([[2,1,5],[3,3,7]], capacity=5)            ->   True
            carPooling([[2,1,5],[3,5,7]], capacity=3)            ->   True
            carPooling([[3,2,7],[3,7,9],[8,3,9]], capacity=11)   ->   True
        '''
        sorted_trips = sorted(trips, key=lambda x: x[1])
        passengers = 0
        pq = []
        
        for x in sorted_trips:
            people, start, end = x
            passengers += people
            heappush(pq, [end, people])
            
            while passengers > capacity:
                old_end, old_pass = heappop(pq)
                
                if old_end <= start:
                    passengers -= old_pass
                else:
                    break
                
            if passengers > capacity:
                return False
            
        return True
