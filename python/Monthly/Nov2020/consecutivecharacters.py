
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 3rd, 2020.
    '''
    def maxPower(self, s: str) -> int:
        '''
        Returns the power of a given string. A string's power is the maximum
        length non-empty substring that contains only one unique character.
        
        Params:
            s - A non-empty string of characters.
            
        Returns:
            int - The power of a string (the longest substring with one unique
                  character).
                  
        Examples:
            maxPower('leetcode)            ->   2
            maxPower('hooraaaaaaaaaaay')   ->   11
            maxPower('tourist')            ->   1
            maxPower('cc')                 ->   2
        '''
        if not s:
            return 0
        
        power = cur = 1
        prev = None
        
        for l in s:
            if l == prev:
                cur += 1
            else:
                power = max(power, cur)
                cur = 1
                
            prev = l
            
        power = max(power,cur)
        return power
