import unittest, sys
sys.path.append('..')
from addsearchword import WordDictionary

class TestAddSearchWord(unittest.TestCase):
    
    def setUp(self):
        self.wd = WordDictionary()
        
    def test_add_word(self):
        self.wd.addWord('bad')
        self.assertEqual(self.wd.trie['b']['a']['d'], {'*': None})
        
        self.wd.addWord('dad')
        self.assertEqual(self.wd.trie['d']['a']['d'], {'*': None})
        
    def test_search(self):
        self.wd.addWord('bad')
        self.wd.addWord('dad')
        self.wd.addWord('mad')
        self.assertFalse(self.wd.search('pad'))
        self.assertTrue(self.wd.search('bad'))
        self.assertTrue(self.wd.search('.ad'))
        self.assertTrue(self.wd.search('b..'))
        
if __name__ == '__main__':
    unittest.main()
