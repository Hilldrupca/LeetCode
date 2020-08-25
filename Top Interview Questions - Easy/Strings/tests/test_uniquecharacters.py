import unittest, sys
sys.path.append('..')
from uniquecharacters import Solution

class TestUniqueCharacters(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().firstUniqChar
        
    def test_equals(self):
        case_one = 'leetcode'
        self.assertEqual(self.s(case_one), 0)
        
        case_two = 'loveleetcode'
        self.assertEqual(self.s(case_two), 2)
        
if __name__ == '__main__':
    unittest.main()
