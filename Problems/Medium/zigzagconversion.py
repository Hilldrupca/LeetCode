
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Returns the zigzag pattern version of a given string. The zigzag string
        is ordered by row appearance. For example, the zigzag pattern of the
        string 'zigzagpattern' over three rows looks like:
        
            z   a   t   n
            
            i z g a t r
            
            g   p   e
        
        Params:
            s - A string to convert to a zigzag pattern.
            
            numRows - An integer number of rows for the pattern.
            
        Returns:
            str - Given string rearranged based on which row characters appear.
                  Returns the string unaltered if numRows is less than 2, or if
                  an empty string is given.
            
        Examples:
            convert('zigzagpattern', 1)   ->   'zigzagpattern'
            convert('zigzagpattern', 3)   ->   'zatnizgatrgpe'
            convert('zigzagpattern', 4)   ->   'zpnigargatezt'
        '''
        if numRows < 2 or not s:
            return s
        
        res = ['' for _ in range(numRows)]
        
        row, inc = 0, 1
        for c in s:
            res[row] += c
            row += inc
            
            if not row or row == numRows - 1:
                inc *= -1
        
        return ''.join(res)
