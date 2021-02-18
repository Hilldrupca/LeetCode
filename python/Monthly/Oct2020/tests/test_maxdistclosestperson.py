import unittest, sys
sys.path.append('..')
from maxdistclosestperson import Solution

class TestMaxDistClosestPerson(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_dist_to_closest(self):
        case_one = [1,0,0,0,1,0,1]
        self.assertEqual(self.s.maxDistToClosest(case_one), 2)
        
        
        case_two = [1,0,0,0]
        self.assertEqual(self.s.maxDistToClosest(case_two), 3)
        
        
        case_three = [0,1]
        self.assertEqual(self.s.maxDistToClosest(case_three), 1)
        
if __name__ == '__main__':
    unittest.main()
