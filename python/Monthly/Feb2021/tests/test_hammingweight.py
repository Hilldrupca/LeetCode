import unittest, sys
sys.path.append('..')
from hammingweight import Solution

class TestHammingWeight(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_hamming_weight(self):
        case_one = 11
        self.assertEqual(self.s.hammingWeight(case_one), 3)
        
        case_two = 128
        self.assertEqual(self.s.hammingWeight(case_two), 1)
        
        case_three = 4294967293
        self.assertEqual(self.s.hammingWeight(case_three), 31)
        
if __name__ == '__main__':
    unittest.main()
