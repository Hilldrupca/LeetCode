
class Solution:
    '''
    LeetCode Monthly Challenge problem for December 28th, 2020.
    '''
    def reachNumber(self, target: int) -> int:
        '''
        Starting from a value of 0, returns the minimum number of moves
        required to reach a target value. During the n-th move (starting from
        1) n can either be add or subtracted from the current value.
        
        Constraints:
            -10**9 <= target <= 10**9
            
        Params:
            target - The target integer to reach.
            
        Returns:
            int - Moves needed to reach target value.
            
        Examples:
            reachNumber(0)    ->   0
            reachNumber(1)    ->   1
            reachNumber(2)    ->   3
            reachNumber(50)   ->   11
        '''
        if not target:
            return 0
        
        target = abs(target)
        
        # binary search to find first sum of natural numbers
        # greater than or equal to target
        l, r = 1, target
        while l < r:
            mid = (l+r)//2
            nat = mid*(mid+1)/2
            
            if nat < target:
                l = mid + 1
            else:
                r = mid
                
        nat_sum = l * (l + 1) / 2
        
        # If nat_sum == target, adding natural numbers can reach target value
        # If the difference between the first natural sum greater than target
        # and target is even, there exists some combination of already added numbers
        # that could be subtracted to reach target value.
        if nat_sum == target or not (nat_sum - target)%2:
            return l
        
        # If one more step is needed to make the difference between natural number sum
        # and target even.
        elif not l%2:
            return l + 1
        
        # If adding the first next step followed by subtracted the second next step
        # reaches the target
        else:
            return l + 2
