from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Returns the length of the longest increasing subsequence in an
        unsorted list of integers. Only considers strictly increasing
        subsequences.
        
        Params:
            nums - A list of integers.
            
        Returns:
            int - The length of the longest increasing subsequence.
            
        Examples:
            lengthOfLIS([[10,9,2,5,3,7,101,18])  ->  4 (2,5,7,101 or 2,3,7,101)
            lengthOfLIS([10,9,2,5,3,4])          ->  3
            lengthOfLIS([[1,3,6,7,9,4,10,5,6])   ->  6
            lengthOfLIS([2,2])                   ->  1
        '''
        def binary_search(active_lis, target):
            low, high = 0, len(active_lis)
            while low < high:
                mid = (low + high)//2
                if active_lis[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            
            return low
        
        lis = []
        for x in nums:
            
            # bisect.bisect_left can also be used here
            idx = binary_search(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
        
        return len(lis)


#[10,9,2,5,3,7,101,18]
#[]
#[0]
#[10,9,2,5,3,4]
#[1,3,6,7,9,4,10,5,6]
#[2,2]
