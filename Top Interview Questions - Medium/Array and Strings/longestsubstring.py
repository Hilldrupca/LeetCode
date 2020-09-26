from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Returns the length of the longest substring without repeating
        characters.
        
        Examples:
            "abcabcbb"   ->   3
            "pwwkew"     ->   3
            " "          ->   1
            "dvdf"       ->   3
        '''
        unique = set()
        sub = deque()
        longest = 0
        for x in s:
            if x in unique:
                longest = max(longest, len(sub))
                popped = ''
                while popped != x:
                    popped = sub.popleft()
                    unique.remove(popped)
                
            sub.append(x)
            unique.add(x)
                
        return max(longest, len(sub))
