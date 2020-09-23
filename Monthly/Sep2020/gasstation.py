from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 22nd, 2020.
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

        Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

        Note:

            If there exists a solution, it is guaranteed to be unique.
            Both input arrays are non-empty and have the same length.
            Each element in the input arrays is a non-negative integer.
        
        Params:
            gas - List of integers representing the amount of gas at each
                  station.
            
            cost - List of integers representing the amount of gas required to
                   travel to the next station.
                   
        Returns:
            int - The starting index if a loop can be made, otherwise -1.
            
        Exampes:
            canCompleteCircuit(gas=[1,2,3,4,5],
                               cost=[3,4,5,1,2])        ->   3
                               
            canCompleteCircuit(gas=[2,3,4],
                               cost=[3,4,3])            ->   -1
        '''
        total_cost = tank = start = 0
        for i in range(len(gas)):
            total_cost += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total_cost > -1 else -1
