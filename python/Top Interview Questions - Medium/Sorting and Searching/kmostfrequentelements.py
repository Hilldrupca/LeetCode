from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Returns the k most frequent elements in nums.
        
        Params:
            nums - A list of integers.
            
            k - Number of elements to return.
            
        Returns:
            List[int] - A list of the most frequent elements.
            
        Examples:
            topKFrequent([1,1,1,2,2,3], 2)   ->   [1,2]
            topKFrequent([1], 1)             ->   [1]
        '''
        counter = {}
        for x in nums:
            counter[x] = counter.get(x, 0) + 1
            
        return sorted(counter, key=counter.__getitem__,reverse=True)[:k]
