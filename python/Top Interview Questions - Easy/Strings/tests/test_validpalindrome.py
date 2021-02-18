import unittest, sys
sys.path.append('..')
from validpalindrome import Solution

class TestValidPalindrom(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
        
    def test_validity(self):
        case_one = 'A man, a plan, a canal: Panama'
        self.assertTrue(self.s.isPalindrome(case_one))
        
        case_two = 'race a car'
        self.assertFalse(self.s.isPalindrome(case_two))
        
if __name__ == '__main__':
    unittest.main()
