
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Return the index of the first occurence of needle in haystack.
        
        Python implementation of C's strstr() and Java's indexOf().
        
        Params:
            haystack - String to be searched.
            
            needle - Substring to search for in haystack.
            
        Returns:
            int - Index of first occurence of needle. Returns -1 if not index
                  is found. If needle is an empty string, returns 0.
                  
        Exampes:
            strStr('hello', 'll')   -> 2
            
            strStr('aaaaa', 'bba')  -> -1
            
            strStr('hi there', '')  -> 0
        '''
        
        return haystack.find(needle) if needle else 0
