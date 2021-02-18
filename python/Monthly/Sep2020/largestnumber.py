from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 25th, 2020.
    '''
    def largestNumber(self, nums: List[int]) -> str:
        '''
        Returns the items of a list of integers arranged to form the
        largest number.
        
        Params:
            nums - A list of integers to arrange.
            
        Returns:
            str - A string version of the largest arranged number.
        '''
        max_len = len(str(max(nums)))
        
        # Sorts numbers after padding to same length. Padding is done with
        # the numbers least significant digit. For example:
        # When sorting ('121', '12'), '12' will be treated as '122'
        res = sorted([str(x) for x in nums],
                     key = lambda x: x + x[-1]*(max_len - len(x)),
                     reverse=True)
        
        # Above sort isn't perfect, but close. Final pass to clean things up.
        for i in range(len(res)-1):
            if res[i+1] + res[i] > res[i] + res[i+1]:
                res[i], res[i+1] = res[i+1], res[i]
                
        res = ''.join(res)
        return res if int(res) else '0'
