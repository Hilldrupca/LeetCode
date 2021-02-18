
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Determines if a string of bracket types is valid.
        
        A string is valid if:
            - Open brackets must be closed by the same type of brackets.
            - Open brackets must be closed in the correct order.
            
        Examples:
            isValid('()')      ->   True
            isValid('()[]{}'   ->   True
            isValid('(]')      ->   False
            isValid('([)]')    ->   False
            isValid('{[]}')    ->   True
        '''
        map = {'(': ')',
               '[': ']',
               '{': '}'}
        paren = []
        for x in s:
            if x in map:
                paren.append(x)
            elif paren and map[paren[-1]] == x:
                paren.pop(-1)
            else:
                return False
                
        return False if paren else True
