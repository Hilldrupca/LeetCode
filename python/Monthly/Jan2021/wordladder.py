from collections import deque
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 9th, 2021.
    '''
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        '''
        Returns the length of the shortest transformation sequence from
        beginWord to endWord such that only one letter can be changed at a
        time, and each intermediate word must exist in wordList.
        
        Constraints:
            1 <= len(beginWord) <= 100
            len(endWord) == len(beginWord)
            1 <= len(wordList) <= 5000
            len(wordList[i]) == len(beginWord)
            beginWord, endWord, and wordList[i] consist of lowercase English
                letters
            beginWord != endWord
            All strings in wordList are unique
            
        Params:
            beginWord - The starting word.
            
            endWord - The goal word to transform to.
            
            wordList - Allowed intermediate words. If endWord is not present,
                       transformation is not possible.
                       
        Returns:
            int - Length of the shortest transformation sequence. Given the
                  transformation sequence ['hit','hot', 'dot','dog','cog']
                  where seq[0] is beginWord, and seq[-1] is endWord, 5 is
                  returned.
                  
        Examples:
            ladderLength('hit','cog'
                         ['hot','dot','dog','lot','log','cog'])   ->   5
            ladderLength('hit','cog',
                         ['hot','dot','dog','lot','log'])         ->   0
        '''
        word_dict = {}
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + '*'+ word[i+1:]
                if temp not in word_dict:
                    word_dict[temp] = []
                    
                word_dict[temp].append(word)
        
        bfs = deque()
        bfs.append((beginWord, 1))
        seen = set([beginWord])
        
        while bfs:
            word, steps = bfs.popleft()
            
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for next_word in word_dict.pop(word[:i] +'*'+ word[i+1:], []):
                    if next_word not in seen:
                        bfs.append((next_word, steps + 1))
                        seen.add(next_word)
        
        return 0
