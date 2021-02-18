import unittest, sys
sys.path.append('..')
from hammingdistance import Solution

class TestHammingDistance(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_hamming_distance(self):
        self.assertEqual(self.s.hammingDistance(x=1, y=4), 2)
        self.assertEqual(self.s.hammingDistance(x=12, y=7), 3)
        self.assertEqual(self.s.hammingDistance(x=16, y=0), 4)
        
if __name__ == '__main__':
    unittest.main()
