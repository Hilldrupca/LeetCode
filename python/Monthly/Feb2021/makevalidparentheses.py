
class Solution:
    '''
    LeetCode Monthly Challenge problem for February 19th, 2021.
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Given a string consisting of '(', ')', and lowercase English
        characters, returns the string with the minimum number of invalid
        parentheses removed.
        
        Constraints:
            1 <= len(s) <= 10**5
            s[i] is one of '(', ')', or lowercase English letter
            
        Params:
            s - A string consisting of '(', ')', and/or lowercase English
                characters.
                
        Returns:
            str - The string with invalid parenthesis removed.
        
        Examples:
            minRemoveToMakeValid('lee(t(c)o)de)')   ->   'lee(t(c)o)de'
            minRemoveToMakeValid('a)b(c)d')         ->   'ab(c)d'
            minRemoveToMakeValid('))((')            ->   ''
            minRemoveToMakeValid('(a(b(c)d)')       ->   'a(b(c)d)'
        '''
        res = []
        paren = []
        
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                paren.append(i)
                res.append('')
            elif c == ')':
                if paren:
                    res[paren.pop()] = '('
                    res.append(c)
                else:
                    res.append('')
            else:
                res.append(c)
                
        return ''.join(res)
