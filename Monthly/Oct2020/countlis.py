from typing import List
from bisect import bisect_left

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 30th, 2020.
    '''
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        Returns the number of longest increasing subsequences.
        
        Params:
            nums - A list of integers.
            
        Returns:
            int - The count of subsequences who have the longest length.
            
        Examples:
            findNumberOfLIS([1,3,5,4,7])   ->   2: [1,3,4,7], and [1,3,5,7]
            findNumberOfLIS([2,2,2,2,2])   ->   5: [2], [2], [2], [2], and [2]
            findNumberOfLIS([])            ->   0: no subsequences
        '''
        if not nums:
            return 0
        
        lis = []
        counts = {0:{}}
        for x in nums:
            # Find the index where the current number should be inserted
            idx = bisect_left(lis, x)
            
            if idx == len(lis):
                # If value is greater than all in current lis, append it
                lis.append(x) 
            else:
                # Update lis index with new lower or equal value
                lis[idx] = x
            
            # Update paths to current value and index
            if not idx:
                # 0 index will always start at a count of 1
                # Increments for repeated values
                counts[0][x] = counts[0].get(x,0) + 1
            else:
                # Ensure index and value exist in dictionary
                counts[idx] = counts.get(idx, {})
                counts[idx][x] = counts[idx].get(x,0)
                
                # Add paths from previous index if they can lead to current
                for k, v in counts[idx-1].items():
                    if k < x:
                        counts[idx][x] += v
            
        # Return the sum of all lis's that have the maxiumum length
        return sum(counts[len(lis)-1].values())
