import unittest, sys
sys.path.append('..')
from removeduplicateletters import Solution

class TestRemoeDuplicateLetters(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().removeDuplicateLetters
        
    def test_remove_duplicate_letters(self):
        self.assertEqual(self.s('bcabc'), 'abc')
        
        self.assertEqual(self.s('cbacdcbc'), 'acdb')
        
if __name__ == '__main__':
    unittest.main()
