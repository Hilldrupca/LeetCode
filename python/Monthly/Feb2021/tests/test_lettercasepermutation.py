import unittest, sys
sys.path.append('..')
from lettercasepermutation import Solution

class TestLetterCasePermutation(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_letter_case_permutation(self):
        self.assertEqual(
            self.s.letterCasePermutation('a1b2'),
            ['a1b2', 'a1B2', 'A1b2', 'A1B2'],
        )
        
        self.assertEqual(
            self.s.letterCasePermutation('3z4'),
            ['3z4', '3Z4'],
        )
        
        self.assertEqual(
            self.s.letterCasePermutation('12345'),
            ['12345'],
        )
        
        self.assertEqual(
            self.s.letterCasePermutation('0'),
            ['0'],
        )
        
if __name__ == '__main__':
    unittest.main()
                                                      
