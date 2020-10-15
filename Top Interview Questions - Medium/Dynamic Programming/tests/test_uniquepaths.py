import unittest, sys
sys.path.append('..')
from uniquepaths import Solution

class TestUniquePaths(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_unique_paths(self):
        self.assertEqual(self.s.uniquePaths(3,7), 28)
        
        self.assertEqual(self.s.uniquePaths(7,3), 28)
        
        self.assertEqual(self.s.uniquePaths(3,2), 3)
        
        self.assertEqual(self.s.uniquePaths(3,3), 6)
        
        self.assertEqual(self.s.uniquePaths(23,12), 193536720)
        
if __name__ == '__main__':
    unittest.main()
