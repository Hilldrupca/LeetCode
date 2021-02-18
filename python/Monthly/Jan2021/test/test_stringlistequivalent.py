import unittest, sys
sys.path.append('..')
from stringlistequivalent import Solution

class TestStringListEquivalent(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_array_strings_are_equal(self):
        case_one = {'word1': ['ab','c'],
                    'word2': ['a','bc']}
        self.assertTrue(self.s.arrayStringsAreEqual(**case_one))
        
        case_two = {'word1': ['a','cb'],
                    'word2': ['ab','c']}
        self.assertFalse(self.s.arrayStringsAreEqual(**case_two))
        
        case_three = {'word1': ['abc','d','defg'],
                      'word2': ['abcddefg']}
        self.assertTrue(self.s.arrayStringsAreEqual(**case_three))
        
if __name__ == '__main__':
    unittest.main()
