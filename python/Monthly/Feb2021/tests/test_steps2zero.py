import unittest, sys
sys.path.append('..')
from steps2zero import Solution

class TestSteps2Zero(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_number_of_steps(self):
        case_one = 14
        self.assertEqual(self.s.numberOfSteps(case_one), 6)
        
        case_two = 8
        self.assertEqual(self.s.numberOfSteps(case_two), 4)
        
        case_three = 123
        self.assertEqual(self.s.numberOfSteps(case_three), 12)
        
if __name__ == '__main__':
    unittest.main()
