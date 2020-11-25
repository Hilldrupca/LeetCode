import unittest, sys
sys.path.append('..')
from smallrepunitdivisiblebyk import Solution

class TestSmallRepunitDivisibleByK(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().smallestRepunitDivByK
        
    def test_smallest_repunit_div_by_k(self):
        self.assertEqual(self.s(0), -1)
        self.assertEqual(self.s(1), 1)
        self.assertEqual(self.s(2), -1)
        self.assertEqual(self.s(3), 3)
        self.assertEqual(self.s(5), -1)
        self.assertEqual(self.s(22229), 22228)
        
if __name__ == '__main__':
    unittest.main()
