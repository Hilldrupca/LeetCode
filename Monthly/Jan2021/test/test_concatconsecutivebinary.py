import unittest, sys
sys.path.append('..')
from concatconsecutivebinary import Solution

class TestConcatConsecutiveBinary(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_concatenated_binary(self):
        self.assertEqual(self.s.concatenatedBinary(1), 1)
        
        self.assertEqual(self.s.concatenatedBinary(3), 27)
        
        self.assertEqual(self.s.concatenatedBinary(12), 505379714)
        
if __name__ == '__main__':
    unittest.main()
