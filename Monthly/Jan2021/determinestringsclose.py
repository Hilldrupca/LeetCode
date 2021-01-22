from collections import Counter

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 22nd, 2021.
    '''
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Determines if two strings are close. Two strings are close if you can
        attain one from the other using any amount of the following operations:
        
            - Swap any two existing characters: abcde -> aecdb
            - Transform every occurence of one existing character into another
              existing character, and do the same with the other character:
              aacabb -> bbcbaa
              
        Constraints:
            1 <= len(word1), len(word2) <= 10**5
            word1 and word2 contain only lowercase English letters
            
        Params:
            word1 - A string of lowercase English letters.
            
            word2 - A string of lowercase English letters.
            
        Returns:
            bool - Returns if the two strings are close using the operations
                   above.
                   
        Examples:
            closeStrings('abc','bc')          ->   True
            closeStrings('a','aa')            ->   False
            closeStrings('cabbba','abbccc')   ->   True
            closeStrings('uau','ssx')         ->   False
        '''
        if len(word1) != len(word2):
            return False
        
        w_one = Counter(word1)
        w_two = Counter(word2)
        
        a = w_one.keys() == w_two.keys()          
        b = sorted(w_one.values()) == sorted(w_two.values())
        
        return a and b
