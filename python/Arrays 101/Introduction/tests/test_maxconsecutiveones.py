import unittest, sys
sys.path.append('..')
from maxconsecutiveones import Solution

class TestMaxConsecutiveOnes(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_max_consecutive_ones(self):
        case_one = [1,1,0,1,1,1]
        self.assertEqual(self.s.findMaxConsecutiveOnes(case_one), 3)
        
        case_two = [1,0,1,1,0,1]
        self.assertEqual(self.s.findMaxConsecutiveOnes(case_two), 2)
        
if __name__ == '__main__':
    unittest.main()
