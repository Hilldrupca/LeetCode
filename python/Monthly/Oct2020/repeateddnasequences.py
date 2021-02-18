from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 17th, 2020.
    '''
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        Returns all 10-letter-long sequences that occur more than once.
        
        Params:
            s - A DNA strand.
            
        Returns:
            List[str] - The substrings of length 10 that appear more than once.
            
        Examples
            findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
                                    ->   ["AAAAACCCCC","CCCCCAAAAA"]
                                    
            findRepeatedDnaSequences('AAAAAAAAAAAAA')
                                    ->   ['AAAAAAAAAA']
        '''
        seq = {}
        res = []
        for x in range(len(s)-9):
            seg = s[x:x+10]
            
            if seg not in seq:
                seq[seg] = 0
                
            elif seq[seg] == 0:
                res.append(seg)
                seq[seg] = 1
            
        return res
