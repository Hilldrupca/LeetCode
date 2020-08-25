import unittest, sys
sys.path.append('..')
from reversestring import Solution

class TestReverseString(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().reverseString
        
    def test_equals(self):
        case_one = ['h','e','l','l','o']
        self.s(case_one)
        self.assertEqual(case_one, ['o','l','l','e','h'])
        
        case_two = ['H','a','n','n','a','h']
        self.s(case_two)
        self.assertEqual(case_two, ['h','a','n','n','a','H'])
        
        case_three = ['C','a','T']
        self.s(case_three)
        self.assertEqual(case_three, ['T','a','C'])
        
if __name__ == '__main__':
    unittest.main()
