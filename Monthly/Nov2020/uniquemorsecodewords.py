from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 22, 2020.
    '''
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        '''
        Given a list of lowercase words, returns the number of unique Morse
        Code representations.
        
        Params:
            words - A list of lowercase words.
            
        Returns:
            int - Number of unique Morse Code representations.
            
        Example:
            words = ['gin', 'zen', 'gig', 'msg']
            uniqueMorseRepresentations(words)   ->   2
        '''
        if not words:
            return 0
        
        letters = {'a': '.-', 'b': '-...', 'c': '-.-.',
                   'd': '-..', 'e': '.', 'f': '..-.',
                   'g': '--.', 'h': '....', 'i': '..',
                   'j': '.---', 'k': '-.-', 'l': '.-..',
                   'm': '--', 'n': '-.', 'o': '---',
                   'p': '.--.', 'q': '--.-', 'r': '.-.',
                   's': '...', 't': '-', 'u': '..-',
                   'v': '...-', 'w': '.--', 'x': '-..-',
                   'y': '-.--', 'z': '--..'}
        
        unique_transforms = set()
        for w in words:
            tran = []
            for l in w:
                tran.append(letters[l])
                
            unique_transforms.add(''.join(tran))
            
        return len(unique_transforms)
