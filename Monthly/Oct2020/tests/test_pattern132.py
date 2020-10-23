import unittest, sys
sys.path.append('..')
from pattern132 import Solution

class TestPattern132(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_132_pattern(self):
        self.assertTrue(self.s.find132pattern([3,1,4,2]))
        self.assertTrue(self.s.find132pattern([-1,3,2,0]))
        
        self.assertFalse(self.s.find132pattern([1,2,3,4]))
        self.assertFalse(self.s.find132pattern([3,2]))
        
if __name__ == '__main__':
    unittest.main()
