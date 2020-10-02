from typing import List
from collections import deque

class Solution:
    '''
    LeetCode Monthly Challenge for October 2nd, 2020.
    '''
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        '''
        Returns a list of all unique combinations of candidates whose sum is
        equal to target. Numbers from candidates may be used multiple times.
        
        Params:
            candidates - A list of integers.
            
            target - The target integer combinations should sum to.
            
        Returns:
            ListList[int]] - A list of list combinations that sum to target.
            
        Examples:
            combinationSum([2,3,6,7], 7)   ->   [[2,2,3], [7]]
            combinationSum([2,3,5], 8)     ->   [[2,3,3], [2,2,2,2], [3,5]]
        '''
        candidates.sort()
        res = []
        for x in candidates:
            bfs = deque()
            bfs.append([x])
            while bfs:
                comb = bfs.popleft()
                comb_sum = sum(comb)
                
                if comb_sum == target:
                    res.append(comb)
                    continue
                    
                start_idx = candidates.index(comb[-1])
                
                # Search for new combinations at index of last comb element.
                for i in range(start_idx, len(candidates)):
                    next_num = candidates[i]
                    if comb_sum + next_num < target:
                        bfs.append(comb + [next_num])
                    elif comb_sum + next_num == target:
                        res.append(comb + [next_num])
                        break
                    else:
                        break
                        
        return res
