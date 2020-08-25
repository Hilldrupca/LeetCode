
class Solution:
    def reverse(self, x: int) -> int:
        '''
        Reverse digits of a signed 32-bit integer. Will return 0 if reversed
        integer is less than -2**31 or greater than 2**31 - 1.
        
        Params:
            x - Signed integer to be reversed.
            
        Returns:
            int - Integer in reversed order, or 0 if reversed integer
                  overflows.
        '''
        res = str(x)
        sign = 1
        
        if res[0] != '-':
            res = res[::-1]
        else:
            res = res[1:][::-1]
            sign = -1
            
        res = int(res) * sign
        
        return res if -2**31 < res < 2**31 - 1 else 0
