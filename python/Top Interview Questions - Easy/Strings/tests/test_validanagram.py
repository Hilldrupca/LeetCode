import unittest, sys
sys.path.append('..')
from validanagram import Solution

class TestValidAnagram(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_validity(self):
        case_one = ['anagram', 'nagaram']
        self.assertTrue(self.s.isAnagram(*case_one))
        
        case_two = ['rat', 'car']
        self.assertFalse(self.s.isAnagram(*case_two))
        
if __name__ == '__main__':
    unittest.main()
