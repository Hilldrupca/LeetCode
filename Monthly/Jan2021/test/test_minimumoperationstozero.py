import unittest, sys
sys.path.append('..')
from minimumoperationstozero import Solution

class TestMinimumOperationsToZero(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_min_operations(self):
        case_one = {'nums': [1,1,4,2,3],
                    'x': 5}
        self.assertEqual(self.s.minOperations(**case_one), 2)
        
        case_two = {'nums': [5,6,7,8,9],
                    'x': 4}
        self.assertEqual(self.s.minOperations(**case_two), -1)
        
        case_three = {'nums': [3,2,20,1,1,3],
                      'x': 10}
        self.assertEqual(self.s.minOperations(**case_three), 5)
        
        case_four = {'nums': [1,1],
                     'x': 3}
        self.assertEqual(self.s.minOperations(**case_four), -1)
        
        case_five = {'nums': [5,2,3,1,1],
                     'x': 5}
        self.assertEqual(self.s.minOperations(**case_five), 1)
        
if __name__ == '__main__':
    unittest.main()
