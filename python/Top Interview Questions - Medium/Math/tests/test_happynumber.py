import unittest, sys
sys.path.append('..')
from happynumber import Solution

class TestHappyNumber(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_is_happy(self):
        self.assertTrue(self.s.isHappy(1))
        self.assertTrue(self.s.isHappy(7))
        self.assertTrue(self.s.isHappy(19))
        
        self.assertFalse(self.s.isHappy(37))
        self.assertFalse(self.s.isHappy(123456789))
        
if __name__ == '__main__':
    unittest.main()
