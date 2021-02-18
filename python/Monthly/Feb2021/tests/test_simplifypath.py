import unittest, sys
sys.path.append('..')
from simplifypath import Solution

class TestSimplifyPath(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_simplify_path(self):
        case_one = "/home/"
        self.assertEqual(self.s.simplifyPath(case_one), '/home')
        
        case_two = "/../"
        self.assertEqual(self.s.simplifyPath(case_two), '/')
        
        case_three = "/home//foo/"
        self.assertEqual(self.s.simplifyPath(case_three), '/home/foo')
        
        case_four = "/a/./b/../../c/"
        self.assertEqual(self.s.simplifyPath(case_four), '/c')
        
if __name__ == '__main__':
    unittest.main()
