import unittest, sys
sys.path.append('..')
from jumpgameIII import Solution

class TestJumpGameIII(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_can_reach(self):
        case_one = {'arr': [4,2,3,0,3,1,2],
                    'start': 5}
        self.assertTrue(self.s.canReach(**case_one))
        
        case_two = {'arr': [4,2,3,0,3,1,2],
                    'start': 0}
        self.assertTrue(self.s.canReach(**case_two))
        
        case_three = {'arr': [3,0,2,1,2],
                      'start': 2}
        self.assertFalse(self.s.canReach(**case_three))
        
        # Empty list or start index out of range
        self.assertFalse(self.s.canReach([], 2))
        self.assertFalse(self.s.canReach([0,1,2], 3))
        self.assertFalse(self.s.canReach([0,1,2], -4))
        
if __name__ == '__main__':
    unittest.main()
