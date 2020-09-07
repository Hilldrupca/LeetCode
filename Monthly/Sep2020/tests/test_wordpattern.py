import unittest, sys
sys.path.append('..')
from wordpattern import Solution

class TestWordPattern(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_equals(self):
        case_one = ['abba', 'dog cat cat dog']
        self.assertTrue(self.s.wordPattern(*case_one))
        
        case_two = ['abba', 'dog cat cat fish']
        self.assertFalse(self.s.wordPattern(*case_two))
        
        case_three = ['aaaa', 'dog cat cat dog']
        self.assertFalse(self.s.wordPattern(*case_three))
        
        case_four = ['aba', 'cat cat cat dog']
        self.assertFalse(self.s.wordPattern(*case_four))
        
if __name__ == '__main__':
    unittest.main()
