import unittest, sys
sys.path.append('..')
from uniquemorsecodewords import Solution

class TestUniqueMorseCodeWords(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().uniqueMorseRepresentations
        
    def test_unique_morse_representations(self):
        
        case_one = ['gin', 'zen', 'gig', 'msg']
        self.assertEqual(self.s(case_one), 2)
        
        case_two = ['gin']
        self.assertEqual(self.s(case_two), 1)
        
        case_three = []
        self.assertEqual(self.s(case_three), 0)
        
if __name__ == '__main__':
    unittest.main()
