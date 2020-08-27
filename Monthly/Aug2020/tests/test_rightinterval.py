import unittest, sys
sys.path.append('..')
from rightinterval import Solution

class TestRightInterval(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().findRightInterval
        
    def test_equals(self):
        case_one = [[1,2]]
        self.assertEqual(self.s(case_one), [-1])
        
        case_two = [[3,4],[2,3],[1,2]]
        self.assertEqual(self.s(case_two), [-1,0,1])
        
        case_three = [[1,4],[2,3],[3,4]]
        self.assertEqual(self.s(case_three), [-1,2,-1])
        
if __name__ == '__main__':
    unittest.main()
