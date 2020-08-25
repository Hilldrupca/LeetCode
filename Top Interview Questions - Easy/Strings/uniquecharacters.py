
class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        Returns the index of the first non-repeating character. Returns
        -1 if there is no such index.
        
        Params:
            s - String in which to find the first non-repeating character.
            
        Returns:
            int - The index of the first non-repeating character, or -1 if
                  no such index exists.
        '''
        if not s:
            return -1
        
        letters = {}
        repeat = set()
        
        for x in range(len(s)):
            
            ch = s[x]
            
            if ch in repeat:
                continue
            
            if ch in letters:
                letters.pop(ch)
                repeat.add(ch)
            
            else:
                letters[ch] = x
                
        
        return min(letters.values()) if letters else -1
