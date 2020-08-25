import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Determine if a string is a palindrome. Only considers alphanumeric
        characters and ignores case.
        
        Params:
            s - String to perform palindrom test.
            
        Returns:
            bool - Whether or not s is a palindrome.
        '''
        
        # Isolate alphanumeric characters
        phrase = re.findall('[a-z0-9]+', s.lower())
        phrase = ''.join(phrase)
        
        return phrase == phrase[::-1]
