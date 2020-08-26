import unittest, sys
sys.path.append('..')
from locatesubstring import Solution

class TestLocateSubstring(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().strStr
        
    def test_equals(self):
        case_one = ['hello', 'll']
        self.assertEqual(self.s(*case_one), 2)
        
        case_two = ['aaaaa', 'bba']
        self.assertEqual(self.s(*case_two), -1)
        
        case_three = ['hi there', '']
        self.assertEqual(self.s(*case_three), 0)
        
if __name__ == '__main__':
    unittest.main()
