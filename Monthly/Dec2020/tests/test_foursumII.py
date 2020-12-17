import unittest, sys
sys.path.append('..')
from foursumII import Solution

class TestFourSumII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_four_sum_count(self):
        case_one = [[1,2],
                    [-2,-1],
                    [-1,2],
                    [0,2]]
        
        self.assertEqual(self.s.fourSumCount(*case_one), 2)
        
        # one empty list
        case_two = [[1,2],
                    [-2,-1],
                    [-1,2],
                    []]
        
        self.assertEqual(self.s.fourSumCount(*case_two), 1)
        
        # two empty lists
        case_three = [[1,2],
                      [-2,-1],
                      [],
                      []]
        
        self.assertEqual(self.s.fourSumCount(*case_three), 2)
        
        # three empty lists
        # essentially counts num of zeroes in non-empty list
        case_four = [[0,0,0],
                     [],
                     [],
                     []]
        
        self.assertEqual(self.s.fourSumCount(*case_four), 3)
        
        # only empty lists
        self.assertEqual(self.s.fourSumCount([],[],[],[]), 0)
        
if __name__ == '__main__':
    unittest.main()
