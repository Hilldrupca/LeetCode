from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 8th, 2021.
    '''
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        '''
        Returns whether or not the two given lists of strings are equivalent
        after elements have been concatentated in order.
        
        Constraints:
            1 <= len(word1), len(word2) <= 10**3
            1 <= len(word1[i]), len(word2[i]) <= 10**3
            1 <= sum(len(word1)), sum(len(word2)) <= 10**3
            word1[i] and wprd2[i] consist of lowercase letters
            
        Params:
            word1 - A list of strings.
            
            word2 - A list of strings.
            
        Returns;
            bool - Whether the given lists of strings are equivalent after in
                   order concatentation.
                   
        Examples:
            arrayStringsAreEqual(['ab','c'],['a','bc'])             ->   True
            arrayStringsAreEqual(['a','cb'],['ab','c'])             ->   False
            arrayStringsAreEqual(['abc','d','defg'],['abcddefg'])   ->   True
        '''
        
        return ''.join(word1) == ''.join(word2)
