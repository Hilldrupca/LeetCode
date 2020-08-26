import unittest, sys
sys.path.append('..')
from commonprefix import Solution

class TestCommonPrefix(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().longestCommonPrefix
        
    def test_equals(self):
        case_one = ['flower','flow','flight']
        self.assertEqual(self.s(case_one), 'fl')
        
        case_two = ['dog','racecar','car']
        self.assertEqual(self.s(case_two), '')
        
        case_three = []
        self.assertEqual(self.s(case_three), '')
        
if __name__ == '__main__':
    unittest.main()
