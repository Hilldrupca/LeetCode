from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Merges and returns overlapping intervals.
        
        Params:
            intervals - A list of integer intervals. ex: [[1,2],[3,4]]
            
        Returns:
            List[List[int]] - A list of overlapping intervals merged/condensed.
            
        Examples:
            merge([[1,3],[2,6],[8,10],[15,18]])   ->   [[1,6],[8,10],[15,18]]
            merge([1,4],[4,5])                    ->   [[1,5]]
            merge([1,4],[5,6])                    ->   [[1,4],[5,6]]
        '''
        if not intervals:
            return []
        
        intervals.sort()
        
        low, high = intervals[0]
        res = []
        for x in intervals:
            if x[0] > high:
                res.append([low,high])
                low, high = x
            else:
                low = min(low, x[0])
                high = max(high, x[1])
                
        res.append([low, high])
                
        return res
