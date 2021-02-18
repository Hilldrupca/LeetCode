import unittest, sys
sys.path.append('..')
from jumpgame import Solution

class TestJumpGame(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_can_jump(self):
        case_one = [2,3,1,1,4]
        self.assertTrue(self.s.canJump(case_one))
        
        
        case_two = [3,2,1,0,4]
        self.assertFalse(self.s.canJump(case_two))
        
        
        case_three = [0]
        self.assertTrue(self.s.canJump(case_three))
        
if __name__ == '__main__':
    unittest.main()
