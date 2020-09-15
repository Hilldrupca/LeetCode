 
class Solution:
    '''
    LeetCode Monthly Challenge problem for September 15th, 2020.
    '''
    def lengthOfLastWord(self, s: str) -> int:
        '''
        Returns the length of the last word in the given string.
        
        Examples:
            lengthOfLastWord('Hello World')   ->   5
            lengthOfLastWord('')              ->   0
            lengthOfLastWord(' ')             ->   0
            lengthOfLastWord('b   a   ')      ->   1
        '''
        words = s.split()
        
        if not words:
            return 0
        
        return len(words[-1])
