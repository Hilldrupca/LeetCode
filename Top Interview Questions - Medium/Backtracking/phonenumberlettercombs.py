from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Returns all possible letter combinations that a given number could
        represent. Digit to letter mappings are similar to those on telephone
        buttons:
            2 - abc
            3 - def
            4 - ghi
            5 - jkl
            6 - mno
            7 - pqrs
            8 - tuv
            9 - wxyz
            
        Params:
            digits - A string version of a number.
            
        Returns:
            List[str] - A list of all letter combinations associated with a
                        number.
                        
        Examples:
            letterCombinations('23')   ->   ['ad',
                                             'ae',
                                             'af',
                                             'bd',
                                             'be',
                                             'bf',
                                             'cd',
                                             'ce',
                                             'cf']
                                             
            letterCombinations('2')    ->   ['a','b','c']
            letterCombinations('')     ->   []
        '''
        if not digits or digits == '0' or digits == '1':
            return []
        
        num_map = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        
        pools = [num_map[x] for x in digits]
        res = [[]]
        for pool in pools:
            res = [x+[y] for x in res for y in pool]
            
        return [''.join(x) for x in res]
