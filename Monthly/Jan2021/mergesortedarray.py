from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 11th, 2021.
    '''
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:
        '''
        Given two sorted lists of integers, merges them in-place into nums1.
        Note that nums1 must have trailing indices to accomodate nums2.
        
        Constraints:
            0 <= n, m <= 200
            1 <= n + m <= 200
            len(nums1) == m + n
            len(nums2) == n
            -10**9 <= nums1[i], nums2[i] <= 10**9
            
        Params:
            nums1 - A sorted list of integers with enough trailing indices to
                    accept nums2.
                    
            m - The length of initialized elements in nums1.
            
            nums2 - A sorted list of integers.
            
            n - The length of nums1.
            
        Returns:
            None - In-place merging with results in nums1.
            
        Examples:
            Given nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3:
                merge(nums1, m, nums2, n)   ->   nums1 = [1,2,2,3,5,6]
            
            Given nums1 = [1], m = 1, nums2 = [], n = 0:
                merge(nums1, m, nums2, n)   ->   nums1 = [1]
                
            Given nums1 = [0], m = 0, nums2 = [1], n = 1:
                merge(nums1, m, nums2, n)   ->   nums1 = [1]
        '''
        m_idx, n_idx = m-1, n-1
        i = m + n -1
        while m_idx >= 0 and n_idx >= 0:
            if nums1[m_idx] > nums2[n_idx]:
                nums1[i] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[i] = nums2[n_idx]
                n_idx -= 1
            
            i -= 1

        while n_idx >= 0:
            nums1[i] = nums2[n_idx]
            i -= 1
            n_idx -= 1
