
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 20th, 2021.
    '''
    def isValid(self, s: str) -> bool:
        '''
        Given a string containing just the characters '(',')','[',']','{','}',
        returns if the input string is valid. Validity is determined by:
        
            Open brackets must be closed by the same type of brackets
            Open brackets must be closed in the correct order
            
        Constraints:
            1 <= len(s) <= 10**4
            s consists of parentheses only '()[]{}'
            
        Params;
            s - A string consisting of only bracket characters.
            
        Returns:
            bool - Returns if the string consists of only valid parentheses.
            
        Examples:
            isValid('()')       ->   True
            isValid('()[]{}')   ->   True
            isValid('(]')       ->   False
            isValid('([)]')     ->   False
            isValid('{[]}')     ->   True
        '''
        start = {'(': ')',
                 '[': ']',
                 '{': '}'}
        
        stack = []
        for x in s:
            if x in start:
                stack.append(x)
            elif stack and start[stack[-1]] == x:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
