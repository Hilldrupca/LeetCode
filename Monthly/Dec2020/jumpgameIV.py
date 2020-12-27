from collections import deque
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 27th, 2020.
    '''
    def minJumps(self, arr: List[int]) -> int:
        '''
        Returns the minimum number of steps to reach the last index starting
        from arr[0]. Allowed moves are the following:
        
            i + 1 where: i + 1 < len(arr)
            i - 1 where: i - 1 >= 0
            j where: arr[i] == arr[j] and i != j
            
        Constraints:
            1 <= len(arr) <= 5 * 10**4
            -10**8 <= arr[i] <= 10**8
            
        Params;
            arr - A list of integers.
            
        Returns:
            int - Minimum steps to reach the last index.
            
        Examples:
            minJumps([7])                                    ->   0
            minJumps([6,1,9])                                ->   2
            minJumps([7,6,9,6,9,6,9,7])                      ->   1
            minJumps([11,22,7,7,7,7,7,7,7,22,13])            ->   3
            minJumps([100,-23,-23,404,100,23,23,23,3,404])   ->   3
        '''
        if not arr:
            return 0
        
        indices = {}
        for i in range(len(arr)):
            if arr[i] not in indices:
                indices[arr[i]] = []
            indices[arr[i]].append(i)
        
        queue = deque([(0,0)])
        visited = set([0])
        
        while queue:
            idx, steps = queue.popleft()
            
            if idx == len(arr)-1:
                return steps
            
            if arr[idx] in indices:
                for n in indices[arr[idx]]:
                    if n not in visited:
                        queue.append((n, steps + 1))
                        visited.add(n)
                del indices[arr[idx]]
            
            if idx and idx-1 not in visited:
                queue.append((idx-1, steps+1))
                visited.add(idx-1)
                
            if idx + 1 not in visited:
                queue.append((idx+1, steps + 1))
                visited.add(idx+1)
