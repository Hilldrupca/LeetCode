import unittest, sys
sys.path.append('..')
from flipimage import Solution

class TestFlipImage(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_flip_and_invert_image(self):
        case_one = [[1,1,0],
                    [1,0,1],
                    [0,0,0]]
        
        exp_ans = [[1,0,0],
                   [0,1,0],
                   [1,1,1]]
        
        self.assertEqual(self.s.flipAndInvertImage(case_one), exp_ans)
        
        case_two = [[1,1,0,0],
                    [1,0,0,1],
                    [0,1,1,1],
                    [1,0,1,0]]
        
        exp_ans = [[1,1,0,0],
                   [0,1,1,0],
                   [0,0,0,1],
                   [1,0,1,0]]
        
        self.assertEqual(self.s.flipAndInvertImage(case_two), exp_ans)
        
if __name__ == '__main__':
    unittest.main()
