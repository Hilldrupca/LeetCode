from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Determine if one string is an anagram of another.
        
        Params:
            s, t - Potential anagram strings.
            
        Returns:
            bool - Whether or not the two strings are anagrams of each other.
        '''
        return Counter(s) == Counter(t)
