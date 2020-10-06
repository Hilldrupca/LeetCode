from typing import List
from collections import deque

class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        '''
        Returns all combinations of n pairs of well-formed parentheses.
        
        Params:
            n - The number of pairs of parentheses per combination.
            
        Returns:
            List[str] - All well-formed parentheses contianing n pairs.
            
        Examples:
            generateParentheses(3)   ->   ["((()))","(()())","(())()",
                                           "()(())","()()()"]
                                           
            generateParentheses(2)   ->   ["(())","()()"]
        '''
        queue = deque()
        queue.append(('(', 1, 0))
        
        res = []
        while queue:
            parens, open_p, close_p = queue.popleft()
            
            if open_p == n and close_p == n:
                res.append(parens)
                continue
            
            if open_p < n:
                queue.append((parens + '(', open_p + 1, close_p))
                
            if close_p < open_p:
                queue.append((parens + ')', open_p, close_p + 1))
                
        return res
