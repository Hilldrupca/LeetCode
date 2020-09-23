import unittest, sys
sys.path.append('..')
from hammingweight import Solution

class TestHammingWeight(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_hamming_weight(self):
        self.assertEqual(self.s.hammingWeight(11), 3)
        self.assertEqual(self.s.hammingWeight(128), 1)
        self.assertEqual(self.s.hammingWeight(4294967293), 31)
        
if __name__ == '__main__':
    unittest.main()
