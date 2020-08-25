from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        Shift array in-place k steps to the right.
        
        Params:
            nums - list of integers
            
            k - number of steps to shift array
            
        Returns:
            None - in-place modification to nums
        
        
        Examples:
            rotate(nums=[1,2,3,4,5,6,7], k=3) modifies
                nums to [5,6,7,1,2,3,4]
                
            rotate(nums=[-1,-100,3,99], k=2) modifies
                nums to [3,99,-1,-100]
        '''
        
        # swap the order of last k elements of nums with
        # the first len(nums)-k items
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
