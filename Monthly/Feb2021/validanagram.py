from collections import Counter

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 11th, 2021.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Returns whether two strings are anagrams of each other.
        
        Params:
            s - A string of characters.
            
            t - A string of characters.
            
        Returns:
            bool - Whether two given strings are anagrams of each other.
            
        Examples:
            isAnagram('anagram', 'nagaram')   ->   True
            isAnagram('rat', 'car')           ->   False
            isAnagram('ab', 'a')              ->   False
        '''        
        return Counter(s) == Counter(t)
