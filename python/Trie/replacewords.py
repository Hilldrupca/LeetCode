from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        '''
        Replaces words in sentence with root words given by dictionary.
        
        Params:
            dictionary - A list of root strings.
            
            sentence - A string of words separated by spaces.
            
        Returns;
            str - The sentence with words replaced by their roots, if given.
            
        Examples:
            d = ['cat','bat','rat']
            s = 'the cattle was rattled by the battery'
            replaceWords(d, s)   ->   'the cat was rat by the bat'
            
            d = ['a','b','c']
            s = 'aadsfasf absbs bbab cadsfafs'
            replaceWords(d, s)   ->   'a a b c'
            
            d = ['a', 'aa', 'aaa', 'aaaa']
            s = 'a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa'
            replaceWords(d, s)   ->   'a a a a a a a a bbb baba a'
        '''
        if not dictionary:
            return sentence
        if not sentence:
            return ''
        
        # Build trie
        trie = {}
        for word in dictionary:
            pre = trie
            for c in word:
                if c not in pre:
                    pre[c] = {}
                pre = pre[c]
                
            pre['*'] = None
            
        # Check for roots to replace words
        res = []
        for word in sentence.split():
            pre = trie
            root = []
            exists = True
            for c in word:
                if '*' in pre:
                    break
                elif c not in pre:
                    exists = False
                    break
                else:
                    root.append(c)
                    pre = pre[c]
                    
            if exists:
                res.append(''.join(root))
            else:
                res.append(word)
                    
        return ' '.join(res)
