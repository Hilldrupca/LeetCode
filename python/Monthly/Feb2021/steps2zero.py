
class Solution:
    '''
    LeetCode Monthly Challenge problem for February 12th, 2021.
    '''
    def numberOfSteps(self, num: int) -> int:
        '''
        Given a number, returns the number of steps to reduce it to zero.
        At each step one of the following may happen:
        
            if number is even, divide by 2
            if number is odd, subtract 1
            
        Constraints:
            0 <= num <= 10**6
            
        Params:
            num - A non-negative integer.
            
        Returns:
            int - Operations to reduce given integer to zero.
            
        Examples:
            numberOfSteps(14)    ->   6
            numberOfSteps(8)     ->   4
            numberOfSteps(123)   ->   12
        '''
        step = 0
        
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
                
            step += 1
            
        return step
