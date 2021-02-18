
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Returns if a number is a happy number.
        
        A happy number is a number who after repeatedly replacing it with the
        sum of the squares of it's digits equals 1. A number is not a happy
        number if this process loops endlessly.
        
        Take 19 for example:
            1**2 + 9**2 = 82
            8**2 + 2**2 = 68
            6**2 + 8**2 = 100
            1**2 + 0**2 + 0**2 = 1
            
        Examples:
            isHappy(19)          ->   True
            isHappy(7)           ->   True
            isHappy(37)          ->   False
            isHappy(123456789)   ->   False
        '''
        seen = set()
        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            next_num = 0
            while n:
                next_num += (n%10)**2
                n //= 10
                
            n = next_num
        
        return True
