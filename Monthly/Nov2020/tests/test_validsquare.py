import unittest, sys
sys.path.append('..')
from validsquare import Solution

class TestValidSquare(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_valid_square(self):
        case_one = [[0,0],[1,1],[1,0],[0,1]]
        self.assertTrue(self.s.validSquare(*case_one))
        
        case_two = [[-1,0],[1,0],[0,1],[0,-1]]
        self.assertTrue(self.s.validSquare(*case_two))
        
        case_three = [[0,0],[1,1],[1,0],[1,1]]
        self.assertFalse(self.s.validSquare(*case_three))
        
        case_four = [[0,0],[5,0],[5,4],[0,4]]
        self.assertFalse(self.s.validSquare(*case_four))
        
        # Contains duplicate points
        case_five = [[0,0],[0,0],[0,0],[0,0]]
        self.assertFalse(self.s.validSquare(*case_five))
        
        # Fewer than four points given
        case_six = [[0,0],[1,1],[1,0],[]]
        self.assertFalse(self.s.validSquare(*case_six))
        
        # No points given
        case_seven = [[], [], [], []]
        self.assertFalse(self.s.validSquare(*case_seven))
        
if __name__ == '__main__':
    unittest.main()
