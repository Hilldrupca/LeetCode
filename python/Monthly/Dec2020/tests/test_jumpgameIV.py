import unittest, sys
sys.path.append('..')
from jumpgameIV import Solution

class TestJumpGameIV(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_min_jumps(self):
        case_one = []
        self.assertEqual(self.s.minJumps(case_one), 0)
                                        
        case_two = [7]
        self.assertEqual(self.s.minJumps(case_two), 0)
                                        
        case_three = [6,1,9]
        self.assertEqual(self.s.minJumps(case_three), 2)
                                        
        case_four = [7,6,9,6,9,6,9,7]
        self.assertEqual(self.s.minJumps(case_four), 1)
                                        
        case_five = [11,22,7,7,7,7,7,7,7,22,13]
        self.assertEqual(self.s.minJumps(case_five), 3)
                                        
        case_six = [100,-23,-23,404,100,23,23,23,3,404]
        self.assertEqual(self.s.minJumps(case_six), 3)

if __name__ == '__main__':
    unittest.main()
