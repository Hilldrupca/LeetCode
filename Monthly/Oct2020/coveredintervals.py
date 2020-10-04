from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge for October 4th, 2020.
    '''
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Returns the number of intervals after removing intervals that are
        covered by another. This will modify the given list. Interval [a,b]
        is covered by interval [c,d] if c <= a and b <= d.
        
        Params:
            intervals - A list of lists containing integer intervals.
            
        Returns:
            int - The number of intervals remaining.
            
        Examples:
            removeCoveredIntervals([[1,4],[3,6],[2,8]])   ->   2
            removeCoveredIntervals([[1,4],[2,3]])         ->   1
            removeCoveredIntervals([[0,10],[5,12]])       ->   2
            removeCoveredIntervals([[1,2],[1,4],[3,4]])   ->   1
        '''
        interval_map = {}
        for x in intervals:
            add = True
            remove = []
            for k, v in interval_map.items():
                if x[0] >= k and x[1] <= v:
                    add = False
                    break
                elif x[0] <= k and x[1] >= v:
                    remove.append(k)
            
            for key in remove:
                interval_map.pop(key)
                
            if add:
                interval_map[x[0]] = x[1]
                
        intervals[:] = [[k, v] for k, v in interval_map.items()]
        return len(intervals)
