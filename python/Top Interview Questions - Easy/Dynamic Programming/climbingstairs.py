
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Determines how many ways to climb a stair case climbing either
        1 or 2 steps with each step. (Fibonacci sequence)
        
        Params:
            n - The total number of steps to climb.
            
        Returns:
            int - The number of ways to climb the stair case.
            
        Examples:
            climbStairs(2)   ->   2
            climbStairs(5)   ->   8
            climbStairs(8)   ->   34
            climbStairs(20)  ->   10946
        '''
        if n < 3:
            return n
        
        prev = 1
        cur = 2
        i = 2
        while i < n:
            prev, cur = cur, prev + cur
            i += 1
            
        return cur
    
        '''
        #The following rounding calculation also works
        
        golden_ratio = (1 + 5**.5)/2
        fib_iter = golden_ratio**(n+1)
        return round(fib_iter/5**.5)
        
        '''
