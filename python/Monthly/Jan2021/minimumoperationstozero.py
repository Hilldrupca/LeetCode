from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 14th, 2021.
    '''
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        Returns the minimum operations to reach zero starting from x. During
        each operation either the leftmost or the rightmost element of nums is
        removed, and subtracted from x. (nums is not altered)
        
        Constraints:
            1 <= len(nums) <= 10**5
            1 <= nums[i] <= 10**4
            1 <= x <= 10**9
            
        Params:
            nums - A list of integers.
            
            x - A starting integer.
            
        Returns:
            int - The minimum operations to reach zero, or -1 if not possible.
            
        Examples:
            minOperations([1,1,4,2,3], 5)       ->   2
            minOperations([5,6,7,8,9], 4)       ->   -1
            minOperations([3,2,20,1,1,3], 10)   ->   5
            minOperations([1,1], 3)             ->   -1
        '''
        left_sums = {0:0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            left_sums[s] = i + 1
        
        min_op = float('inf') if x not in left_sums else left_sums[x]
        
        s = 0
        r = len(nums) - 1
        while r >=0 and s <= x:
            s += nums[r]
            
            if x - s in left_sums and left_sums[x-s] < r:
                min_op = min(min_op, len(nums) - r + left_sums[x-s])
            
            r -= 1
            
        return min_op if min_op != float('inf') else -1
