from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        In-place merge and sort of two lists.
        
        Instructions say to assume nums1 will have enough extra space
        (end elements are zeroes) to accomidate elements of nums2.
        
        Params:
            nums1 - A list of integers with enough ending zeroes to accomodate
                    nums2.
                    
            m - Index of nums1 where nums2 elements should start.
            
            nums2 - A list of integers to merge into nums1.
            
            n - Number of elements in nums2.
            
        Returns:
            None - In-place merge and sort. Results are found in nums1.
            
        Example:
            merge([1,2,3,0,0,0], m=3, [2,5,6], n=3)  ->  nums1 == [1,2,2,3,5,6]
        '''
        while n > 0:
            n -= 1
            nums1[m+n] = nums2[n]
            
        nums1.sort()
