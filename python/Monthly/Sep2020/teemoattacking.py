from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 26th, 2020.
    '''
    def findPoisonedDuration(self, timeSeries: List[int],
                             duration: int) -> int:
        '''
        In LOL world, there is a hero called Teemo and his attacking can make
        his enemy Ashe be in poisoned condition. Now, given the Teemo's
        attacking ascending time series towards Ashe and the poisoning time
        duration per Teemo's attacking, you need to output the total time that
        Ashe is in poisoned condition.

        You may assume that Teemo attacks at the very beginning of a specific
        time point, and makes Ashe be in poisoned condition immediately.
        
        Params:
            timeSeries - A list of integers of attack time points.
            
            duration - The integer duration of poison status.
            
        Returns:
            int - The total time poisoned.
            
        Examples:
            findPoisonedDuration([1,4], 2)   ->   4
            findPoisonedDuration([1,2], 2)   ->   3
        '''
        if not timeSeries:
            return 0
        
        res = 0
        for x in range(1, len(timeSeries)):
            if timeSeries[x] - timeSeries[x-1] < duration:
                res += timeSeries[x] - timeSeries[x-1]
            else:
                res += duration
                
        return res + duration
