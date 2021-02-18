from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 16th, 2021.
    '''
    def letterCasePermutation(self, S: str) -> List[str]:
        '''
        Given a string consisting only of letter or digits, returns all
        possible permutations of its characters if they can be uppercase
        or lowercase.
        
        Constraints:
            S will be a string with length between 1 and 12
            S will consist only of letters or digits
            
        Params:
            S - A string of letters or digits.
            
        Returns:
            List[str] - All possible permuations of given string. Each
                        characters may be changed to uppercase or lowercase.
                        
        Examples:
            letterCasePermutation('a1b2')    ->   ['a1b2', 'a1B2', 'A1b2', 'A1B2']
            letterCasePermutation('3z4')     ->   ['3z4', '3Z4']
            letterCasePermutation('12345')   ->   ['12345']
            letterCasePermutation('0')       ->   ['0']
        '''
        combs = []
        stack = [""]
        
        while stack:
            so_far = stack.pop()
            idx = len(so_far)
            
            if idx == len(S):
                combs.append(so_far)
                continue
                
            char = S[idx]
            
            if char.isalpha():
                stack.append(so_far + char.upper())
                stack.append(so_far + char.lower())
            else:
                stack.append(so_far + char)
                
        return combs
