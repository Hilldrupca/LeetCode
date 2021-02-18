import unittest, sys
sys.path.append('..')
from validanagram import Solution

class TestValidAnagram(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_is_anagram(self):
        case_one = {'s': 'anagram',
                    't': 'nagaram'}
        self.assertTrue(self.s.isAnagram(**case_one))
        
        case_two = {'s': 'rat',
                    't': 'car'}
        self.assertFalse(self.s.isAnagram(**case_two))
        
        case_three = {'s': 'ab',
                      't': 'a'}
        self.assertFalse(self.s.isAnagram(**case_three))
        
if __name__ == '__main__':
    unittest.main()
