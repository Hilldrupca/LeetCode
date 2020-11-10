
class WordDictionary:
    '''
    A trie implementation of add and search word data structure.
    '''
    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
            
        trie['*'] = None

    def search(self, word: str) -> bool:
        """
        Checks if a word has been added. Each occurence of '.' in a word
        represents any letter.
        
        Examples:
            Assume 'bad', 'dad', and 'mad' have already been added to
            WordDictionary, wd:
            
            wd.search('pad')   ->   False
            wd.search('bad')   ->   True
            wd.search('.ad')   ->   True
            wd.search('b..')   ->   True
        """
        found = False
        def dfs(idx, prefix) -> None:
            nonlocal found
            if found or prefix is None:
                return
            if idx == len(word):
                found = '*' in prefix
                return
            if word[idx] == '.':
                for pre in prefix.values():
                    dfs(idx+1, pre)
            elif word[idx] in prefix:
                dfs(idx+1, prefix[word[idx]])
        
        dfs(0, self.trie)
        return found
