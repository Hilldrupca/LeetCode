import unittest, sys
sys.path.append('..')
from basetencomplement import Solution

class TestBaseTenComlement(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_bitwise_complement(self):
        self.assertEqual(self.s.bitwiseComplement(5), 2)
        self.assertEqual(self.s.bitwiseComplement(7), 0)
        self.assertEqual(self.s.bitwiseComplement(10), 5)
        self.assertEqual(self.s.bitwiseComplement(0), 1)
        self.assertEqual(self.s.bitwiseComplement(1), 0)
        
if __name__ == '__main__':
    unittest.main()
