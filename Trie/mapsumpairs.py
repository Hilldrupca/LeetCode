from collections import deque

class MapSum:
    '''
    A trie implementation of mapsum.
    '''
    def __init__(self):
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        '''
        Inserts a word-val pair into the trie. If the key already exists,
        the value will be overridden.
        '''
        trie = self.trie
        for c in key:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
            
        trie['*'] = val

    def sum(self, prefix: str) -> int:
        '''
        Returns the sum of all word-val pairs that begin with prefix.
        
        Example:
            Given the following word-value pairs are already inserted:
                car: 1
                cartoon: 2
                cartridge: 3
                
            sum('car')     ->   6
            sum('cart')    ->   5
            sum('carto')   ->   2
            sum('cat')     ->   0
        '''
        trie = self.trie
        for c in prefix:
            if c in trie:
                trie = trie[c]
            else:
                return 0
            
        mapsum = 0
        bfs = deque([trie])
        while bfs:
            pre = bfs.popleft()
            if type(pre) == int:
                mapsum += pre
            else:
                bfs.extend(pre.values())
            
        return mapsum
