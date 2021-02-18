import unittest, sys
sys.path.append('..')
from generatedarraymax import Solution

class TestGeneratedArrayMax(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_get_maximum_generated(self):
        
        self.assertEqual(self.s.getMaximumGenerated(0), 0)
        
        self.assertEqual(self.s.getMaximumGenerated(2), 1)
        
        self.assertEqual(self.s.getMaximumGenerated(3), 2)
        
        self.assertEqual(self.s.getMaximumGenerated(7), 3)
        
        self.assertEqual(self.s.getMaximumGenerated(100), 21)
        
if __name__ == '__main__':
    unittest.main()
