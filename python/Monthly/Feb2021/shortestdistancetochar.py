from bisect import bisect_left
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 7th, 2021.
    '''
    def shortestToChar(self, s: str, c: str) -> List[int]:
        '''
        Given a string, s, and a target character, c, returns a list of the
        shortest distances from each character to the target character.
        
        Constraints:
            1 <= len(s) <= 10**4
            s[i] and c are lowercase English letters
            c occurs at least once in s
            
        Params:
            s - A string of lowercase English letters.
            
            c - A target lowercase English letter.
            
        Returns:
            List[int] - The shortest distances from each character to the
                        target character.
                        
        Examples:
            shortestToChar('loveleetcode', 'e')  ->  [3,2,1,0,1,0,0,1,2,2,1,0]
            shortestToChar('aaab', 'b')          ->  [3,2,1,0]
            shortestToChar('aaba', 'b')          ->  [2,1,0,1]
        '''
        res = [0] * len(s)
        c_idx = []
        
        for idx, l in enumerate(s):
            if l == c:
                c_idx.append(idx)
                
        for i in range(len(res)):
            if s[i] != c:
                idx = bisect_left(c_idx, i)
                
                if not idx:
                    res[i] = c_idx[idx] - i
                elif idx == len(c_idx):
                    res[i] = i - c_idx[idx-1]
                else:
                    res[i] = min(c_idx[idx] - i,
                              i - c_idx[idx-1])
                    
        return res
