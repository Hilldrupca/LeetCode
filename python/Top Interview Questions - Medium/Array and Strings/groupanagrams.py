from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Returns anagrams in a list of strings grouped together. Order of output
        is not guaranteed.
        
        Example:
            groupAnagrams(["eat","tea","tan","ate","nat","bat"]) -> 
            
                [["bat"],["nat","tan"],["ate","eat","tea"]]
        '''
        sorted_words = defaultdict(list)
        
        for x in strs:
            word = ''.join(sorted(x))
            sorted_words[word].append(x)
            
        return list(sorted_words.values())
