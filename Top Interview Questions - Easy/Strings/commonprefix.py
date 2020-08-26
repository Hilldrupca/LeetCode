from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Finds the longest common prefix among the words in strs.
        
        Params:
            strs - List of words to check prefixes.
            
        Returns:
            str - Longest commong prefix for words in strs.
            
        Examples:
            lcp = longestCommonPrefix
            
            lcp(['flower','flow','flight'])   ->   'fl'
            
            lcp(['dog','racecar','car'])      ->   ''
            
            lcp([''])                         ->   ''
        '''
        
        if not strs:
            return ''
        
        res = ''
        
        for x in range(0, len(strs[0])):
            sub = strs[0][:x+1]
            for word in strs[1:]:
                if not word[:x+1] == sub:
                    return res
                
            res = sub
            
        return res
