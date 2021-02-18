from collections import defaultdict, deque
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 14,2020.
    '''
    def partition(self, s: str) -> List[List[str]]:
        '''
        Returns all possible palindrome partitions of a given string. A
        palindrome partition can be as small as a single character. Result
        order may not be sorted.
        
        Constraints:
            1 <= len(s) <= 16
            s contains only lowercase English letters.
            
        Params:
            s - A string of lowercase English letters.
            
        Returns:
            List[List[str]] - A list of all possible palindrome partitions of
                              a given string.
        
        Examples:
            partition('aab')       ->   [['aa','b'],
                                         ['a','a','b']]
                                         
            partition('a')         ->   [['a']]
            
            partition('racecar')   ->   [['racecar'],
                                         ['r','aceca','r'],
                                         ['r','a','cec','a','r'],
                                         ['r','a','c','e','c','a','r']]
        '''
        if not s:
            return []
        
        start_indices = defaultdict(list)
        
        def expand(l, r, phrase, index_map):
            '''Maps palindrome substrings to index in s'''
            while l > -1 and r < len(phrase) and phrase[l] == phrase[r]:
                index_map[l].append(phrase[l:r+1])
                l, r = l - 1, r + 1
                
        # Populate start_indices with palindromes of even and odd lengths
        for i in range(len(s)):
            expand(i,i,s, start_indices)
            expand(i,i+1,s, start_indices)
        
        res = []
        queue = deque([([],0)])
        while queue:
            pal, length = queue.popleft()
            
            if length == len(s):
                res.append(pal)
                continue
            
            for sub in start_indices[length]:
                queue.append((pal+[sub], length+len(sub)))
                
        return res
