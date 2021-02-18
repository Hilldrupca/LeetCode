import unittest, sys
sys.path.append('..')
from dominorotationequal import Solution

class TestDominoRotationEqual(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution().minDominoRotations
        
    def test_min_domino_rotations(self):
        case_one = {'A': [2,1,2,4,2,2],
                    'B': [5,2,6,2,3,2]}
        
        self.assertEqual(self.s(**case_one), 2)
        
        
        case_two = {'A': [3,5,1,2,3],
                    'B': [3,6,3,3,4]}
        
        self.assertEqual(self.s(**case_two), -1)
        
        
        case_three = {'A': [1,1,1,1,1],
                      'B': [1,1,1,1,1]}
        
        self.assertEqual(self.s(**case_three), 0)
        
        
        case_four = {'A': [1,2,2,1,2,1,2,1,2],
                     'B': [1,2,1,1,1,1,2,1,2]}
        
        self.assertEqual(self.s(**case_four), -1)
        
        
        case_five = {'A': [1,2,3,4,6],
                     'B': [6,6,6,6,5]}
        
        self.assertEqual(self.s(**case_five), 1)
        
        
        case_six = {'A': [2,1,1,3,2,1,2,2,1],
                    'B': [3,2,3,1,3,2,3,3,2]}
        
        self.assertEqual(self.s(**case_six), -1)
        
if __name__ == '__main__':
    unittest.main()
