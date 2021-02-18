from typing import List
from collections import deque

class StreamChecker:
    '''
    LeetCode Monthly Challenge problem for August 23rd, 2020
    
    
    Personal implementation at the very bottom. Not as fast, but uses less
    memory and is easier to read.
    '''
    def __init__(self, words: List[str]):
        '''
        Construct a trie using the reversed form of each word from a list
        of words, "apple" would be treated as "elppa"
        
        Usage:
            StreamChecker(['quick', 'brown', 'fox',...])
        
        Params:
            words - a list of strings
            
        '''
        self.letters = deque()
        self.fragments = {}
        for w in words:
            f = self.fragments
            for ch in w[::-1]:
                if ch not in f:
                    f[ch] = {}
                f = f[ch]
            f['end'] = w
         
    def query(self, letter: str) -> bool:
        '''
        Check if the last added letters spell one of the words added
        during class construction.
        
        Params:
            letter - newest letter to check spelling against
            
        Returns:
            bool - whether or not newest letters spell one of the
                   stored words.
                   
        Examples:
            stream = StreamChecker(['cd', 'f', 'kl'])
            stream.query('a') -> False
            stream.query('b') -> False
            stream.query('c') -> False
            stream.query('d') -> True
            stream.query('e') -> False
            stream.query('f') -> True
        '''
        self.letters.appendleft(letter)
        
        f = self.fragments
        for ch in self.letters:
            if 'end' in f:
                return True
            
            if ch not in f:
                return False
            
            f = f[ch]    
            
        if 'end' in f:
            return True

        
    '''
    def __init__(self, words: List[str]):
        self.words = tuple(words)
        self.letters = ''
        
    def query(self, letter: str) -> bool:
        self.letters += letter
        return self.letters.endswith(self.words)        
    '''
