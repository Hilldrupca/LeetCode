import unittest, sys
sys.path.append('..')
from implementtrie import Trie

class TestImplementTrie(unittest.TestCase):
    
    def setUp(self):
        self.t = Trie()
        
    def test_insert(self):
        self.t.insert('apple')
        self.assertEqual(self.t.trie['a']['p']['p']['l']['e'], {'*': None})
        
    def test_search(self):
        self.t.insert('apple')
        self.assertTrue(self.t.search('apple'))
        self.assertFalse(self.t.search('app'))
        
        self.t.insert('app')
        self.assertTrue(self.t.search('app'))
        
    def test_startswith(self):
        self.t.insert('apple')
        self.assertTrue(self.t.startsWith('app'))
        self.assertFalse(self.t.startsWith('ac'))
        
if __name__ == '__main__':
    unittest.main()
