from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Move all 0's to the end of a list in-place while maintaining the
        relative order of the non-zero elements.
        
        Params:
            nums - list of numbers
            
        Returns:
            Nothing - in-place modification to nums
            
        Example:
            nums = [0,1,0,3,12]
            moveZeroes(nums)
            print(nums) -> [1,3,12,0,0]            
        '''
        
        nums.sort(key=bool, reverse=True)
        
        
        # the following is a custom implementation
        
        #front = 0
        #z = 0
        #for x in nums:
            #if x:
                #nums[front] = x
                #front += 1
            #else:
                #z += 1
             
        #idx = -1
        #while z:
            #nums[idx] = 0
            #z -= 1
            #idx -= 1
