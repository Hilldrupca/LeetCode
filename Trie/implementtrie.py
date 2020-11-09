
class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
            
        trie['*'] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.trie
        for c in word:
            if c in trie:
                trie = trie[c]
            else:
                return False
            
        return '*' in trie
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        """
        trie = self.trie
        for c in prefix:
            if c in trie:
                trie = trie[c]
            else:
                return False
            
        return True
