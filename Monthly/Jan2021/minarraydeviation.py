from heapq import heapify, heappushpop
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 30th, 2021.
    '''
    def minimumDeviation(self, nums: List[int]) -> int:
        '''
        Given a list of integers, returns the minimum difference between the
        highest and lower numbers after any number of the following operations:
        
            if nums[i] is even - nums[i] //= 2
            
            if nums[i] is odd - nums[i] *= 2
            
        Constraints:
            2 <= len(nums) <= 10**5
            1 <= nums[i] <= 10**9
        
        Params:
            nums - A list of positive integers.
            
        Returns:
            int - The minimum deviation after any number of approved
                  operations.
                  
        Examples:
            minimumDeviation([1,2,3,4])      ->   1
            minimumDeviation([4,1,5,20,3])   ->   3
            minimumDeviation([2,10,8])       ->   3
        '''
        nums = [-x * 2 if x % 2 else -x for x in nums]
        heapify(nums)
        
        l = -max(nums)
        res = -nums[0] - l
        while not nums[0] % 2:
            l = min(l, -nums[0] // 2)
            heappushpop(nums, nums[0] // 2)
            res = min(res, -nums[0] - l)
            
        return res
    
    
    #def minimumDeviation_SortedList(self, nums: List[int]) -> int:
        #'''
        #Solves same problem as self.minimumDeviation, except uses SortedList
        #from the sortedcontainers module instead of the heapq module.
        #'''
        #from sortedcontainers import SortedList
        
        #n = SortedList()
        #n.update(nums)
        
        #res = n[-1] - n[0]
        
        #while n[0] % 2:
            #x = n.pop(0)
            #n.add(x*2)
            #res = min(res, n[-1] - n[0])
        
        #while not n[-1] % 2:
            #x = n.pop(-1)
            #n.add(x // 2)
            #res = min(res, n[-1] - n[0])
        
        #return res
