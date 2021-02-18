from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        '''
        Reverse in-place a string given as a list of individual characters.
        
        Params:
            s - List of individual string characters.
            
        Returns:
            None - In-place reversal of s.
            
        Examples:
            reverseString(['h','e','l','l','o') -> ['o','l','l','e','h']
            
            reverseString(['C','a','t']) -> ['t','a','C']
        '''
        s.reverse()
        
