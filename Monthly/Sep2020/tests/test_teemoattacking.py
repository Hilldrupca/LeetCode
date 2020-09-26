import unittest, sys
sys.path.append('..')
from teemoattacking import Solution

class TestTeemoAttacking(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_find_poisoned_duration(self):
        case_one = {'timeSeries': [1,4],
                    'duration': 2}
        ans_one = self.s.findPoisonedDuration(**case_one)
        self.assertEqual(ans_one, 4)
        
        case_two = {'timeSeries': [1,2],
                    'duration': 2}
        ans_two = self.s.findPoisonedDuration(**case_two)
        self.assertEqual(ans_two, 3)
        
if __name__ == '__main__':
    unittest.main()
