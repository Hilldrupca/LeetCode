
class Solution:
    '''
    LeetCode Monthly Challenge problem for August 19th, 2020.
    '''
    def toGoatLatin(self, S: str) -> str:
        '''
        A sentence S is given, composed of words separated by spaces. Each
        word consists of lowercase and uppercase letters only.

        We would like to convert the sentence to "Goat Latin" (a made-up
        language similar to Pig Latin.)

        The rules of Goat Latin are as follows:

            If a word begins with a vowel (a, e, i, o, or u), append "ma" to
            the end of the word. For example, the word 'apple' becomes
            'applema'.
        
            If a word begins with a consonant (i.e. not a vowel), remove the
            first letter and append it to the end, then add "ma".
            For example, the word "goat" becomes "oatgma".
        
            Add one letter 'a' to the end of each word per its word index in
            the sentence, starting with 1. For example, the first word
            gets "a" added to the end, the second word gets "aa" added to the
            end and so on.

        Params:
            S - String of one or more words. May only contain upper and
                lowercase letters, and sppaces.
        
        Returns:
            String - The final sentence representing the conversion from S
                     to Goat Latin. 
        '''
        
        vowels = set(['a','A','e','E','i','I','o','O','u','U'])
        
        words = S.split(' ')
        
        for x in range(len(words)):
            word = words[x]
            
            # If word does not begin with a vowel
            if word[0] not in vowels:
                
                # Move first letter to end
                word = word[1:] + word[0]
            
            # Add 'maa' and additional 'a' based on index
            words[x] = word + 'maa' + 'a' * x
            
        return ' '.join(words)
 
