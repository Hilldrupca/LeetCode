from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:
        '''
        In-place merge of two sorted integers lists to form one sorted list.
        
        Params:
            nums1: A sorted list of integers with right padding equal to the
                   length of nums2.
                   
            m - The number of elements initialized in nums1, excludes right
                padding which is initialized to zeroes.
            
            nums2: A sorted list of integers.
            
            n - The number of elements initialized in nums2.
            
        Returns:
            None - In-place merge.
            
        Examples:
            merge(nums1 = [1,2,3,0,0,0], m = 3,
                  nums2 = [2,5,6], n = 3)         ->   nums1 == [1,2,2,3,5,6]
                  
            merge(nums1 = [4,5,6,0,0,0], m = 3,
                  nums2 = [1,2,3], n = 3)         ->   nums1 == [1,2,3,4,5,6]
        '''
        while n:
            if m and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
