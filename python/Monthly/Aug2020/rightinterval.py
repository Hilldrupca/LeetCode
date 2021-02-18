from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        '''
        Checks a list of intervals i for an interval j whose start point is
        bigger than or equal to the end point of interval i. For each
        interval i, the minimum interval j's index is stored and returned as
        a list. If there is not interval j for a given interval i, -1 is stored
        instead.
        
        Each interval starting point is assumed unique.
        
        
        Params:
            intervals - List of intervals, such as [[1,2],[3,4],[5,6]]
            
        Returns:
            list - A list of interval j indices.
            
        Exampes:
            If intervals = [[1,2]], [-1] would be returned since [1,2] is the
                           only interval.
                        
            If intervals = [[3,4],[2,3],[1,2]], [-1,0,1] would be returned. For
                           [3,4], no other interval begins with 4 or greater
                           (-1). For [2,3], only [3,4] begins with 3 or greater
                           (0). Finally for [1,2], [2,3] is chosen (1) because
                           it's starting point 2 is less than [3,4]'s staring
                           point.
        '''
        if len(intervals) == 1:
            return [-1]
        
        # Store indices for each starting point
        indices = {y[0]: x for x,y in enumerate(intervals)}
        
        # Store sorted copy of intervals for later binary search
        inter = sorted(intervals)
        
        res = []
        for x in intervals:
            idx = bisect.bisect_left(inter, [x[1],x[0]]) # Binary search
            if idx == len(intervals):
                res.append(-1) # No intervals start >= x[1]
            else:
                res.append(indices[inter[idx][0]])
                
        return res
