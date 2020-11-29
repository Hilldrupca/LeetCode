from typing import List
from collections import deque

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 29th, 2020.
    '''
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        Given a list of integers, and a starting index, returns whether
        any index with a value of zero can be reached. The next reachable
        spaces at any point are determined by:
            
            i + arr[i] or i - arr[i]
        
        Params:
            arr - A list of positive integers.
            
            start - Integer starting index.
            
        Returns:
            bool - If an index with a value of zero can be reached.
            
        Examples:
            canReach([4,2,3,0,3,1,2], 5)   ->   True
            canReach([4,2,3,0,3,1,2], 0)   ->   True
            canReach([3,0,2,1,2], 2)       ->   False
        '''
        if not arr or start >= len(arr) or start < -len(arr):
           return False
        
        visited = set()
        visited.add(start)
        bfs = deque()
        bfs.append(start)
        
        while bfs:
            cur = bfs.popleft()
            
            if not arr[cur]:
                return True
            
            plus, minus = cur + arr[cur], cur - arr[cur]
            if plus < len(arr) and plus not in visited:
                bfs.append(plus)
                visited.add(plus)
                
            if minus > -1 and minus not in visited:
                bfs.append(minus)
                visited.add(minus)
                
        return False
