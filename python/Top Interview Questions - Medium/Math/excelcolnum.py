
class Solution:
    def titleToNumber(self, s: str) -> int:
        '''
        Returns a column title into a column number. For example, column 'D' in
        a spreadsheet is equivalent ot column 4.
        
        Params:
            s - A column title, e.g. 'A' or 'BC'
            
        Returns:
            int - The given column title converted to a column number.
            
        Examples:
            titleToNumber('A')         ->   1
            titleToNumber('AB')        ->   28
            titleToNumber('ZY')        ->   701
            titleToNumber('FXSHRXW')   ->   2147483647
        '''
        if not s.isupper():
            s = s.upper()
            
        col = 0
        n = len(s)-1
        for l in s:
            base = ord(l)-64
            col += base*26**n
            n -= 1
            
        return col
