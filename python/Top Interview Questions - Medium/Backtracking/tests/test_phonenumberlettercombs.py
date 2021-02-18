import unittest, sys
sys.path.append('..')
from phonenumberlettercombs import Solution

class TestPhoneNumberLetterCombs(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_letter_combinations(self):
        ans_one = self.s.letterCombinations('23')
        expected_combs = ['ad','ae','af','bd','be','bf','cd','ce','cf']
        
        for x in expected_combs:
            self.assertIn(x, ans_one)
            
            
        ans_two = self.s.letterCombinations('2')
        expected_combs = ['a','b','c']
        
        for x in expected_combs:
            self.assertIn(x, ans_two)
            
        
        # Check for empty combinations
        self.assertEqual(self.s.letterCombinations('0'), [])
        self.assertEqual(self.s.letterCombinations('1'), [])
        self.assertEqual(self.s.letterCombinations(''), [])
        
if __name__ == '__main__':
    unittest.main()
