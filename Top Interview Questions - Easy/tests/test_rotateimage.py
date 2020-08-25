import unittest, sys
sys.path.append('..')
from rotateimage import Solution

class TestRotateImage(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().rotate
        
    def test_equals(self):
        case_one = [[1,2,3],
                    [4,5,6],
                    [7,8,9]]
        self.s(case_one)
        
        case_one_exp = [[7,4,1],
                        [8,5,2],
                        [9,6,3]]
        
        self.assertEqual(case_one, case_one_exp)
        
        case_two = [[ 5, 1, 9,11],
                    [ 2, 4, 8,10],
                    [13, 3, 6, 7],
                    [15,14,12,16]]
        self.s(case_two)
        
        case_two_exp = [[15,13, 2, 5],
                        [14, 3, 4, 1],
                        [12, 6, 8, 9],
                        [16, 7,10,11]]
        
        self.assertEqual(case_two, case_two_exp)
        
if __name__ == '__main__':
    unittest.main()
