import unittest, sys
sys.path.append('..')
from countprimes import Solution

class TestCountPrime(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_count_primes(self):
        self.assertEqual(self.s.countPrimes(10), 4)
        self.assertEqual(self.s.countPrimes(20), 8)
        self.assertEqual(self.s.countPrimes(100000), 9592)
        self.assertEqual(self.s.countPrimes(500000), 41538)
        
if __name__ == '__main__':
    unittest.main()
