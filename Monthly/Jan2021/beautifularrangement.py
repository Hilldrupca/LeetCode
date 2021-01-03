
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 3rd, 2020.
    '''
    def countArrangement(self, n: int) -> int:
        '''
        Returns the number of beautiful arrangements for numbers 1 to n. A 
        beautiful arrangement is a list constructed using the numbers 1 to n
        that satisfies one of the following (ith position means 1 <= i <= n):
        
            The number at the ith position is divisible by i
            i is divisible by the number at the ith position
            
        Constraints:
            1 <= n <= 15
            
        Params:
            n - The max number to use for the beautiful arrangements.
            
        Returns:
            int - Number of possible beautiful arrangements with n as max
                  number.
                  
        Examples:
            countArrangement(1)   ->   1
            countArrangement(2)   ->   2
            countArrangement(3)   ->   3
            countArrangemntt(4)   ->   8
        '''
        def dfs(nums, memo):
            if len(nums) == 1:
                return 1
            
            if nums in memo:
                return memo[nums]
            
            res = 0
            for idx, n in enumerate(nums):
                if not len(nums) % n or not n % len(nums):
                    res += dfs(nums[:idx] + nums[idx+1:], memo)
                    
            memo[nums] = res
            return res
        
        memo = {}
        nums = tuple(range(1, n+1))
        return dfs(nums, memo)
