from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 18th, 2020.
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Given a list of intervals, returns a list with overlapping intervals
        merged. Does not modify original list.
        
        Params:
            intervals - A list of start-end integer pair lists.
            
        Returns:
            List[List[int]] - A list of merged overlapping intervals.
            
        Examples:
            merge([[1,3],[2,6],[8,10],[15,18]])   ->   [[1,6],[8,10],[15,18]]
            merge([[1,4],[2,3]])                  ->   [[1,4]]
        '''
        if not intervals:
            return []
        
        sorted_intervals = sorted(intervals)
        res = []
        start, end = sorted_intervals[0]
        for s, e in sorted_intervals:
            if s > end:
                res.append([start, end])
                start, end = s, e
            elif e > end:
                end = e
                
        res.append([start, end])
        
        return res
