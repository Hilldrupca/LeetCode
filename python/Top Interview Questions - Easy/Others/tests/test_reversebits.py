import unittest, sys
sys.path.append('..')
from reversebits import Solution

class TestReverseBits(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_reverse_bits(self):
        self.assertEqual(self.s.reverseBits(43261596), 964176192)
        self.assertEqual(self.s.reverseBits(4294967293), 3221225471)
        
if __name__ == '__main__':
    unittest.main()
