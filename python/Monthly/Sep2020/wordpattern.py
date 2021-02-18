
class Solution:
    '''
    LeetCode Monthly Challenge problem for September 7th, 2020.
    '''
    def wordPattern(self, pattern: str, phrase: str) -> bool:
        '''
        Determines whether the given phrase follows the given pattern.
        
        Params:
            pattern - A string of characters. Example: 'abba'.
            
            phrase - A string of word(s) that may be separated by a space.
            
        Returns:
            bool - Whether or not phrase followed the pattern. Will return
                   False if the word length of phrase does not equal the
                   length of pattern.
            
        Examples:
            wordPattern('abba', 'dog cat cat dog')   ->   True
            wordPattern('abba', 'dog cat cat fish')  ->   False
            wordPattern('aaaa', 'dog cat cat dog')   ->   False
            wordPattern('aba', 'cat cat cat dog')    ->   False
        '''
        split_phrase = phrase.split()
        if len(pattern) != len(split_phrase):
            return False
        
        set_pat = set(pattern)
        set_phrase = set(split_phrase)
        set_zipped = set(zip(pattern, split_phrase))
        
        return len(set_pat) == len(set_phrase) == len(set_zipped)
