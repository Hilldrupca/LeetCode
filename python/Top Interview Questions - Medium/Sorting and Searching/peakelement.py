from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Returns the index of a peak element in a given list. A peak element is
        defined as num[i-1] < nums[i] > nums[i+1]. The start and end indices
        are only compared to which ever side is within the index range.
        
        Params:
            nums - A list of integers.
            
        Returns:
            int - An index of a peak element.
            
        Examples:
            findPeakElement([1,2,3,1])         ->   2
            findPeakElement([1,2,1,3,5,6,4])   ->   1 or 5
        '''
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end)//2
            if mid > 0 and nums[mid-1] > nums[mid]:
                end, mid = mid, (mid + start)//2
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                start, mid = mid, (mid + end)//2
            else:
                break
                
        return mid
