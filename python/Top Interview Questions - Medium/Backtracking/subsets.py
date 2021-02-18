from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Return all possible subsets (power set) of a set of distinct integers.
        
        Params:
            nums - A list of distinct integers.
            
        Returns:
            List[List[int]] - A list of lists of integer subsets. (Power set)
            
        Example:
            subsets([1,2,3])   ->   [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        '''
        res = []
        end = 2**len(nums)
        for x in range(end):
            count = 0
            temp = []
            while x:
                if x%2:
                    temp.append(nums[count])
                
                count += 1
                x //= 2
                
            res.append(temp)
            
        return res
