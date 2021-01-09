import unittest, sys
sys.path.append('..')
from wordladder import Solution

class TestWordLadder(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_ladder_length(self):
        case_one = {'beginWord': 'hit',
                    'endWord': 'cog',
                    'wordList': ['hot','dot','dog','lot','log','cog']}
        self.assertEqual(self.s.ladderLength(**case_one), 5)
        
        # wordList does not contain endWord
        case_two = {'beginWord': 'hit',
                    'endWord': 'cog',
                    'wordList': ['hot','dot','dog','lot','log']}
        self.assertEqual(self.s.ladderLength(**case_two), 0)
        
        case_three = {'beginWord': 'leet',
                      'endWord': 'code',
                      'wordList': ['lest','leet','lose','code',
                                   'lode','robe','lost']}
        self.assertEqual(self.s.ladderLength(**case_three), 6)
        
if __name__ == '__main__':
    unittest.main()
