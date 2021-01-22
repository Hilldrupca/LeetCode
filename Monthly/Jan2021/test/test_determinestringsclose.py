import unittest, sys
sys.path.append('..')
from determinestringsclose import Solution

class TestDetermineStringsClose(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_close_strings(self):
        case_one = {'word1': 'abc',
                    'word2': 'bca'}
        self.assertTrue(self.s.closeStrings(**case_one))
        
        case_two = {'word1': 'a',
                    'word2': 'aa'}
        self.assertFalse(self.s.closeStrings(**case_two))
        
        case_three = {'word1': 'cabbba',
                      'word2': 'abbccc'}
        self.assertTrue(self.s.closeStrings(**case_three))
        
        case_four = {'word1': 'cabbba',
                     'word2': 'aabbss'}
        self.assertFalse(self.s.closeStrings(**case_four))
        
        case_five = {'word1': 'uau',
                     'word2': 'ssx'}
        self.assertFalse(self.s.closeStrings(**case_five))
        
if __name__ == '__main__':
    unittest.main()
