import unittest, sys
sys.path.append('..')
from buddystrings import Solution

class TestBuddyStrings(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_buddy_strings(self):
        self.assertTrue(self.s.buddyStrings('ab','ba'))
        self.assertTrue(self.s.buddyStrings('aa','aa'))
        self.assertTrue(self.s.buddyStrings('aaaaaaabc','aaaaaaacb'))
        
        self.assertFalse(self.s.buddyStrings('ab','ab'))
        self.assertFalse(self.s.buddyStrings('','aa'))
        self.assertFalse(self.s.buddyStrings('abab','baba'))
        
if __name__ == '__main__':
    unittest.main()
