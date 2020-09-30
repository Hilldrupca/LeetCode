from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge for September 29th, 2020.
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Given a non-empty string s and a dictionary wordDict containing a
        list of non-empty words, determine if s can be segmented into a
        space-separated sequence of one or more dictionary words. A word in
        wordDict may be used multiple times.
        
        Params:
            s - String to be checked for segmentation.
            
            wordDict - A list of unique strings.
            
        Returns:
            bool - Whether or not s can be segmented using the words in
                   wordDict.
                   
        Examples:
            wordBreak('leetcode',['leet','code'])                     ->  True
            wordBreak('applepenapple',['apple','pen'])                ->  True
            wordBreak('catsandog',['cats','dog','sand','and','cat'])  ->  False
        '''
        words = {}
        for x in wordDict:
            words[x] = len(x)
            
        pos_tracker = [1]+[0]*len(s)
        for i in range(len(s)):
            if pos_tracker[i]:
                for word, length in words.items():
                    if i+length-1 < len(s) and s[i:i+length] == word:
                        pos_tracker[i+length] = 1
                        
        return True if pos_tracker[-1] else False
