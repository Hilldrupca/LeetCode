from collections import Counter

class Solution:
    '''
    LeetCode Monthly Challenge problem for September 24th, 2020.
    '''
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        Returns the one letter difference between s and t. String t is a
        shuffled version of s with an extra letter added at a random position.
        
        Example:
            findTheDifference(s='abcd', t='abcde')   ->   'e'
        '''
        
        # If only one letter difference, diff will only contain one key-value pair.
        diff = Counter(t) - Counter(s)
        return diff.popitem()[0]
