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
        
        # Populate all indices associated with each number
        indices = {}
        for i, num in enumerate(arr):
            if num not in indices:
                indices[num] = []
            indices[num].append(i)
        
        # Perform breadth first search for last index
        queue = deque([(0,0)])
        visited = set([0])
        while queue:
            idx, steps = queue.popleft()
            
            if idx == len(arr)-1:
                return steps
            
            # Visit other indices associated with arr[idx] if haven't already
            if arr[idx] in indices:
                for n in indices[arr[idx]]:
                    if n not in visited:
                        queue.append((n, steps + 1))
                        visited.add(n)
                        
                # Delete to prevent repeat checks if arr[idx] repeats
                del indices[arr[idx]]
            
            # Visit index prior if haven't already
            if idx and idx-1 not in visited:
                queue.append((idx-1, steps+1))
                visited.add(idx-1)
                
            # Visit index after if haven't already
            if idx + 1 not in visited:
                queue.append((idx+1, steps + 1))
                visited.add(idx+1)
