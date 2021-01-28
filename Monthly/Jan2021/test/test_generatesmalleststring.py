import unittest, sys
sys.path.append('..')
from generatesmalleststring import Solution

class TestGenerateSmallestString(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_get_smallest_string(self):
        self.assertEqual(self.s.getSmallestString(3, 27), 'aay')
        
        self.assertEqual(self.s.getSmallestString(5, 73), 'aaszz')
        
if __name__ == '__main__':
    unittest.main()
