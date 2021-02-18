import unittest, sys
sys.path.append('..')
from ksumpairs import Solution

class TestKSumPairs(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_max_operations(self):
        case_one = {'nums': [1,2,3,4],
                    'k': 5}
        self.assertEqual(self.s.maxOperations(**case_one), 2)
        
        case_two = {'nums': [3,1,3,4,3],
                    'k': 6}
        self.assertEqual(self.s.maxOperations(**case_two), 1)
        
if __name__ == '__main__':
    unittest.main()
