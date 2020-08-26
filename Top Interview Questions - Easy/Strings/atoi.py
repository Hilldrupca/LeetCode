import re

class Solution():
    def myAtoi(self, phrase: str) -> int:
        '''
        Convert a string to an integer as long as it begins with
        the following format:
            - 0 or more whitespace characters
            - 0 or 1 of '-' or '+'
            - 1 or more digits
            
        Decimals will be counted until the decimal place. For '3.14', only the
        '3' will be matched.
        
        Params:
            phrase - String to convert to an integer.
            
        Returns:
            int - Returns an integer if it follows the format above, otherwise
                  returns 0.
                  
        Examples:
            myAtoi('42')        -> 42
            myAtoi('     -42')  -> -42
            myAtoi('3.14')      -> 3
            myAtoi('+-42')      -> 0
            myAtoi('Jan 1')     -> 0
        '''
        if not phrase:
            return 0
        
        cleaned = re.findall('^\s*([-+]?\d+)', phrase)
        
        if not cleaned:
            return 0
        
        # Will convert signed strings to the appropriate signed integer
        res = int(cleaned[0])
        
        if res < -2**31:
            return -2**31
        if res > 2**31-1:
            return 2**31-1
        
        return res
